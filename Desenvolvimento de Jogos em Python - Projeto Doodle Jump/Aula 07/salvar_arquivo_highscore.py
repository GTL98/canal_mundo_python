# --- Importar as bibliotecas --- #
import os
import sys


def salvar_arquivo_highscore(nome_arquivo):
    # --- O arquivo fica salvo sempre na mesma pasta do .exe --- #
    if getattr(sys, 'frozen', False):
        # --- Se estiver rodando como .exe --- #
        diretorio_base = sys._MEIPASS
    else:
        # --- Se estiver rodando como .py --- #
        diretorio_base = os.path.dirname('.')

    return os.path.join(diretorio_base, nome_arquivo)