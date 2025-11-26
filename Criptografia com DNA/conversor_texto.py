# --- Importar o JSON --- #
import json

# --- Abrir o arquivo base2txt.json --- #
with open ('base2txt.json', 'r', encoding='utf-8') as f:
    base2txt = json.load(f)

# --- Abrir o arquivo txt2base.json --- #
with open ('txt2base.json', 'r', encoding='utf-8') as f:
    txt2base = json.load(f)

# --- Entrada --- #
entrada = ''''''

# --- Saída --- #
saida = ''

# --- Verificar se será criptografa ou decriptografada a mensagem --- #
modo = 'decrip'

# --- Criptografar a mensagem --- #
if modo == 'crip':
    for caractere in entrada:
        saida += txt2base[caractere]
    # --- Mostrar a saída --- #
    print(saida)

# --- Decriptografar a mensagem --- #
if modo == 'decrip':
    for i in range(len(entrada)):
        k = entrada[i*4:i*4+4]
        if len(k) == 4:
            saida += base2txt[k]
    # --- Mostrar a saída --- #
    print(saida.replace('\\n', '\n').replace('\\t', '\t'))
