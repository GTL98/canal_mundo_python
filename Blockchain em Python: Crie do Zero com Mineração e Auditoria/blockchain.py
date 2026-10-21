# --- Importar as bibliotecas --- #
import os
import json

# --- Importar o bloco --- #
from block import Block


class Blockchain:
    def __init__(self):
        # --- Nome do arquivo --- #
        self.nome_arquivo = 'blockchain.json'

        # --- Dificuldade --- #
        self.dificuldade = 3

        # --- Se existir é somente para carregar --- #
        if os.path.exists(self.nome_arquivo):
            self.carregar_arquivo()

        # --- Se não existir é para criar o arquivo com o bloco gênesis --- #
        else:
            self.corrente = [self.criar_bloco_genesis()]
            self.salvar()

    def criar_bloco_genesis(self):
        # --- O bloco gênesis é criado manualmente, pois não há bloco anterior --- #
        return Block(0, 'Bloco Gênesis', '0')

    def obter_ultimo_bloco(self):
        # --- Pegar o último bloco atual da corrente --- #
        return self.corrente[-1]

    def adicionar_bloco(self, novo_bloco):
        # --- O novo bloco pega o hash do último bloco --- #
        novo_bloco.hash_anterior = self.obter_ultimo_bloco().hash

        # --- Calcular o hash do novo bloco --- #
        novo_bloco.hash = novo_bloco.calcular_hash()

        # --- Ao invés de somente calcular a hash, calcular o nouce --- #
        novo_bloco.minerar(self.dificuldade)

        # --- Engatar o novo bloco na corrente --- #
        self.corrente.append(novo_bloco)

        # --- Salvar o bloco --- #
        self.salvar()

    def salvar(self):
        # --- Pegar a corrente e transformar cada bloco em um dicionário --- #
        dados_corrente = []
        for bloco in self.corrente:
            dados_corrente.append(bloco.to_dict())

        # --- Salvar as informações no arquivo JSON --- #
        with open(self.nome_arquivo, 'w') as f:
            json.dump(dados_corrente, f, indent=4)

    def carregar_arquivo(self):
        # --- Abrir o arquivo --- #
        with open(self.nome_arquivo, 'r') as f:
            dados_corrente = json.load(f)

            # --- Reiniciar a corrente limpa --- #
            self.corrente = []

            # --- Para cada bloco no texto, recriar o bloco --- #
            for bloco_dic in dados_corrente:
                # --- Pegar os dados do arquivo --- #
                bloco_recuperado = Block(
                    bloco_dic['indice'],
                    bloco_dic['dados'],
                    bloco_dic['hash_anterior']
                )

                # --- Restaurar as informações exatas do passado --- #
                bloco_recuperado.timestamp = bloco_dic['timestamp']
                bloco_recuperado.hash = bloco_dic['hash']
                bloco_recuperado.nouce = bloco_dic['nouce']

                # --- Armazenar de volta à corrente --- #
                self.corrente.append(bloco_recuperado)

    def corrente_valida(self):
        # --- Começar pelo segundo bloco (o bloco gênesis não precisa) --- #
        for i in range(1, len(self.corrente)):
            bloco_atual = self.corrente[i]
            bloco_anterior = self.corrente[i - 1]

            # --- Pergunta 1: O hash está intacto? --- #
            # --- Se calcular o hash agora com os dados atuais, ele bate com o hash salvo? --- #
            if bloco_atual.hash != bloco_atual.calcular_hash():
                print(f'ALERTA DE FRAUDE: Os dados do bloco #{bloco_atual.indice} foram alterados!')
                return False

            # --- Pergunta 2: A corrente está conectada? --- #
            # --- O "hash_anterior" deste bloco bate com o hash real do bloco de trás? --- #
            if bloco_atual.hash_anterior != bloco_anterior.hash:
                print(f'ALERTA DE FRAUDE: A conexão entre o bloco #{bloco_atual.indice} e o bloco #{bloco_anterior.indice} quebrou!')
                return False

        print('VERIFICADO: A blockchain está 100% segura!')
        return True