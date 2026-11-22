# --- Importar as bibliotecas --- #
import os
import hashlib
from block import Block
from datetime import datetime
from blockchain import Blockchain


class SistemaCuradoria:
    def __init__(self, pasta_cofre='cofre_arquivos'):
        self.blockchain = Blockchain()
        self.pasta_cofre = pasta_cofre

        # --- Criar a pasta do cofre --- #
        os.makedirs(self.pasta_cofre, exist_ok=True)

    def gerar_hash_bytes(self, conteudo_bytes):
        # --- Gerar o SHA-256 diretamente dos bytes do arquivo --- #
        return hashlib.sha256(conteudo_bytes).hexdigest()

    def registrar_documento(self, **kwargs):
        # --- Calcular o hash do arquivo principal --- #
        hash_arquivo = self.gerar_hash_bytes(kwargs['conteudo_bytes'])

        # --- Salvar o arquivo no cofre usando o ID, versão e início do hash --- #
        _, extensao = os.path.splitext(kwargs['nome_arquivo'])
        nome_cofre = f'{kwargs["id_documento"]}_{kwargs["versao"]}_{hash_arquivo[:8]}{extensao}'
        caminho_cofre = os.path.join(self.pasta_cofre, nome_cofre)

        with open(caminho_cofre, 'wb') as f:
            f.write(kwargs['conteudo_bytes'])

        # --- Dicionário com os metadados para colocar no bloco --- #
        dados_curadoria = {
            'id_documento': kwargs['id_documento'],
            'nome_original': kwargs['nome_arquivo'],
            'versao': kwargs['versao'],
            'curador': kwargs['curador'],
            'status': kwargs['status'],  # Revisão, Aprovado, Rejeitado
            'observacao': kwargs['observacao'],
            'data_registro': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'hash_arquivo': hash_arquivo,
            'caminho_cofre': caminho_cofre
        }

        # --- Criar e minerar o bloco --- #
        proximo_indice = self.blockchain.obter_ultimo_bloco().indice + 1
        novo_bloco = Block(proximo_indice, dados_curadoria, '')
        self.blockchain.adicionar_bloco(novo_bloco)

        return novo_bloco

    def listar_ids_documentos(self):
        # --- Retorna uma lista sem duplicatas de todos os IDs registrados --- #
        ids = set()

        # --- Pular o bloco gênesis --- #
        for bloco in self.blockchain.corrente[1:]:
            if isinstance(bloco.dados, dict) and 'id_documento' in bloco.dados:
                ids.add(bloco.dados['id_documento'])

        return sorted(list(ids))

    def obter_historico_documento(self, id_documento):
        # --- Filtrar todos os blocos pertencentes a um documento específico --- #
        historico = []
        for bloco in self.blockchain.corrente[1:]:
            if isinstance(bloco.dados, dict) and bloco.dados.get('id_documento') == id_documento:
                historico.append({
                    'indice_bloco': bloco.indice,
                    'hash_bloco': bloco.hash,
                    'nouce': bloco.nouce,
                    **bloco.dados  # desempacotar o dicionário dentro do outro
                })

        return historico

    def obter_arquivo_seguro(self, registro):
        # --- Cruzar o arquivo físico do cofre com a hash --- #
        caminho = registro[0]['caminho_cofre']

        if not os.path.exists(caminho):
            return False, 'O arquivo desapareceu do cofre', None

        with open(caminho, 'rb') as f:
            conteudo_atual = f.read()

        hash_atual = self.gerar_hash_bytes(conteudo_atual)

        if hash_atual != registro[0]['hash_arquivo']:
            return False, 'ALERTA DE FRAUDE: O arquivo no cofre foi modificado!', None

        return True, 'Arquivo íntegro e verificado!', conteudo_atual

    def auditar_arquivo_externo(self, conteudo_bytes):
        # --- Garantir que ninguém alterou a própria blockchain --- #
        if not self.blockchain.corrente_valida():
            return {
                'valido': False,
                'motivo': 'CRÍTICO: A estrutura da Blockchain foi corrompida!'
            }

        # --- Calcular o hash do arquivo enviado --- #
        hash_suspeito = self.gerar_hash_bytes(conteudo_bytes)

        # --- Procurar o hash na corrente --- #
        for bloco in self.blockchain.corrente[1:]:
            if isinstance(bloco.dados, dict) and bloco.dados.get('hash_arquivo') == hash_suspeito:
                return {
                    'valido': True,
                    'motivo': 'Documento autêntico encontrado na Blockchain!',
                    'indice_bloco': bloco.indice,
                    'detalhes': bloco.dados
                }

        return {
            'valido': False,
            'motivo': 'Arquivo não encontrado ou sofreu alteração após registro.'
        }