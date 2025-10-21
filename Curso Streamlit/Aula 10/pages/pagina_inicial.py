# --- Importar o Streamlit --- #
import streamlit as st


def pagina_inicial():
    """Função responsável por criar a página inicial."""
    st.title('Página Inicial')
    st.write('Bem-vindo à nossa aplicação modular Streamlit!')
    st.info('Use a barra lateral para navegar entre as páginas.')