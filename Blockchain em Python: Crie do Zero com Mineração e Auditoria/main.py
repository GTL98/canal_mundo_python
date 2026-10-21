# --- Importar o bloco e a blockchain --- #
from block import Block
from blockchain import Blockchain


# --- Criar a blockchain --- #
blockchain = Blockchain()
indice = blockchain.corrente[-1].indice

print(f'Minerando o bloco #{indice + 1}...')
blockchain.adicionar_bloco(Block(indice + 1, 'Enviando 10 moedas para o João', ''))

print(f'Minerando o bloco #{indice + 2}...')
blockchain.adicionar_bloco(Block(indice + 2, 'Enviando 5 moedas para Maria', ''))

# --- Verificar a integridade da blockchain --- #
print('\nIniciando auditoria na blockchain...')
blockchain.corrente_valida()

# --- Ataque hacker --- #
print('\nATAQUE HACKER EM ANDAMENTO')
blockchain.corrente[3].dados = 'Enviando 100 moedas para Maria'
print('Iniciando auditoria da rede após ataque...')
blockchain.corrente_valida()
blockchain.corrente[3].hash = blockchain.corrente[3].calcular_hash()
blockchain.corrente_valida()
