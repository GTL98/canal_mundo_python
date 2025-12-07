# --- Importar o Streamlit --- #
import streamlit as st

# --- Criar um menu de navegação das páginas --- #
pg = st.navigation(
    [st.Page('./pages/pdf_merger.py', title='PDF Merger'),
     st.Page('./pages/visualizador_pdf.py', title='Visualizador de PDF')]
)
pg.run()