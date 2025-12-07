# --- Importar a biblioteca do PDF --- #
from pypdf import PdfReader


def obter_pdfs(arquivos: list) -> list:
    """
    Função responsável por obter os arquivos PDFs.
    :param arquivos: Arquivos PDFs
    :return: Lista com os arquivos PDFs.
    """
    # --- Lista com os arquivos PDFs --- #
    pdfs = []

    # --- Carregar os arquivos PDFs --- #
    for arquivo in arquivos:
        # --- Carregar o arquivo --- #
        pdf_carregado = PdfReader(arquivo)
        pdfs.append(pdf_carregado)

    return pdfs
