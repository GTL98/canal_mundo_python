# --- Importar o JSON --- #
import json

# --- Abrir o arquivo com a criptografia --- #
with open('base2txt.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# --- Dicionário para a decriptografia --- #
dic = {caractere: nt for nt, caractere in dados.items()}

#  --- Criar o arquivo JSON com a criptografia --- #
with open('txt2base.json', 'w', encoding='utf-8') as f:
    json.dump(
        dic,
        f,
        ensure_ascii=False,
        indent=4
    )