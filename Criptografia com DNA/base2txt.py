# --- Importar as bibliotecas --- #
import json
from random import randint
from itertools import product

# --- Lista com as bases nucleicas --- #
bases = ['A', 'T', 'C', 'G']

# --- Combinações --- #
combinacoes = product(bases, repeat=4)

# --- Lista com as combinacoes --- #
lista_combinacoes = [combinacao for combinacao in combinacoes]

# --- String com os caracteres --- #
caracteres = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789áàãâéêíîóõôúûçÁÀÃÂÉÊÍÎÕÔÚÛÇ',.!?:;<> \\n\\t-+*/()[]{}_%=#\\'''

# --- Lista com os nucleotídeos selecionados --- #
nts = []

# --- Iterar sobre as combinações --- #
for _ in lista_combinacoes:
    n = randint(0, len(lista_combinacoes) - 1)
    i = ''.join(lista_combinacoes[n])
    if i not in nts and len(nts) < len(caracteres):
        nts.append(i)

# --- Criar um dicionário com a criptografia --- #
dic_combinacoes = {nt: caractere for nt, caractere in zip(nts, caracteres)}

# --- Salvar o dicionário em um arquivo JSON --- #
with open('base2txt.json', 'w', encoding='utf-8') as f:
    json.dump(
        dic_combinacoes,
        f,
        ensure_ascii=False,
        indent=4
    )
