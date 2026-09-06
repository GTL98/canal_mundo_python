# --- Importar as bibliotecas --- #
import os
import sys


def caminho_assets(caminho_relativo):
    # --- Saber tanto o caminho dos assets para .py quanto para o .exe --- #
    try:
        # --- Se for um .exe, o PyInstaller armazena o caminho interno no _MEIPASS --- #
        caminho_base = sys._MEIPASS
    except Exception:
        # --- Se for o script .py, usa a pasta raiz do projeto --- #
        caminho_base = os.path.abspath('.')

    return os.path.join(caminho_base, caminho_relativo)