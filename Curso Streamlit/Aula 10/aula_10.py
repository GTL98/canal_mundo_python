# --- Importar o Streamlit --- #
import streamlit as st

# --- Importar as páginas --- #
from pages import pagina_inicial, analise_dados

st.sidebar.title('Navegação')
pagina = st.sidebar.radio(
    label='Ir para:',
    options=['Página Inicial', 'Análise']
)

# --- Verificar qual página foi selecionada --- #
if pagina == 'Página Inicial':
    pagina_inicial.pagina_inicial()
if pagina == 'Análise':
    analise_dados.analise_dados()