# --- Importar o Streamlit --- #
import streamlit as st

# --- Título principal da página --- #
st.title('Minha primeira aplicação Streamlit!')

# --- Cabeçalho --- #
st.header('Bem-vindo ao mundo Streamlit!')

# --- Subcabeçalho --- #
st.subheader('Vamos explorar essa ferramenta incrível!')

# --- Texto genérico --- #
st.write('Este é um texto simples usando o st.write()')

# --- Texto formatado com Markdown --- #
st.markdown('''
Este é um exemplo de **Markdown** no Streamlit.
Podemos usar **negrito**, *itálico* e até mesmo **listas**:
* Item 1
* Item 2
''')

# --- Texto literal --- #
st.text('Este é um texto puro, sem formatação.')