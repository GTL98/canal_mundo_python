# --- Importar as bibliotecas --- #
import streamlit as st
from obter_pdfs import obter_pdfs
from juntar_pdf import juntar_pdf

# --- Configurações da página --- #
st.set_page_config(page_title='PDF Merger', layout='centered')

# --- Título da página --- #
st.title('PDF Merger')

# --- Campo para selecionar o nome do arquivo final --- #
nome_arquivo_final = st.text_input(
    label='Nome do arquivo',
    placeholder='Digite o nome do arquivo final'
)

# --- Upload dos arquivos --- #
upload = st.file_uploader(
    label='Escolha os arquivos em PDF',
    type='pdf',
    accept_multiple_files=True
)

# --- Criar as colunas --- #
colunas = st.columns(5)

# --- Botão para juntar os  PDFs --- #
with colunas[2]:
    botao = st.button('Juntar')
    if botao:
        # --- Carregar os PDFs --- #
        pdfs = obter_pdfs(upload)

        # --- Juntar os PDFs --- #
        pdf_junto = juntar_pdf(pdfs)

        # --- Baixar o PDF --- #
        st.download_button(
            label='Download',
            data=pdf_junto,
            file_name=f'{nome_arquivo_final}.pdf',
            mime='application/octet-stream'
        )