# --- Importar as bibliotecas --- #
import time
import hashlib


class Block:
    def __init__(self, indice, dados, hash_anterior):
        self.nouce = 0
        self.dados = dados
        self.indice = indice
        self.timestamp = time.time()
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        # --- Juntar todas as informações do bloco em um único texto --- #
        bloco_string = f'{self.indice}{self.timestamp}{self.dados}{self.hash_anterior}{self.nouce}'

        # --- Gerar a hash pelo SHA-256 --- #
        return hashlib.sha256(bloco_string.encode()).hexdigest()

    def to_dict(self):
        # --- Transformar as propriedades do bloco em um dicionário de dados --- #
        return {
            'indice': self.indice,
            'timestamp': self.timestamp,
            'dados': self.dados,
            'hash_anterior': self.hash_anterior,
            'nouce': self.nouce,
            'hash': self.hash
        }

    def minerar(self, dificuldade):
        # --- Regra: uma string de zeros baseada na dificuldade --- #
        objetivo = '0' * dificuldade

        # --- Loop para encontrar a hash que começa com '0' * dificuldade --- #
        while not self.hash.startswith(objetivo):
            # --- Aumentar o chute e recalcular a hash --- #
            self.nouce += 1
            self.hash = self.calcular_hash()

        print(f'Bloco minerado! Hash: {self.hash} | Tentativas (Nouce): {self.nouce}')