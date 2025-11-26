# --- Importar o JSON --- #
import json

# --- Abrir o arquivo txt2base.json --- #
with open ('txt2base.json', 'r', encoding='utf-8') as f:
    txt2base = json.load(f)

# --- Abrir um arquivo qualquer --- #
with open('txt2base.py', 'r', encoding='utf-8') as f:
    conteudo = f.read()

# --- Saída --- #
saida = ''

# --- Criptografar o arquivo --- #
for caractere in conteudo:
    saida += txt2base[caractere]

# --- Mostrar a saída --- #
print(saida)