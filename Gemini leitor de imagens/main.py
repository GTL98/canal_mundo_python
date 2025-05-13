# --- Importar as bibliotecas para o projeto --- #
from PIL import Image
import streamlit as st
import google.generativeai as genai

# --- Importar as funções criadas --- #
from funcoes import *

# --- Configurações do site --- #
st.set_page_config(
    page_title='Leitor de imagens',
    page_icon=':robot:',
    layout='centered'
)

# --- Título da página --- #
st.title('Leitor de imagens')
st.caption('Feito com Gemini')

# --- Alocar a chave API no site --- #
if 'chave_api' not in st.session_state:
    chave_api = st.sidebar.text_input('Chave API', type='password')
    if chave_api.startswith('AI'):
        st.session_state.chave_api = chave_api
        genai.configure(api_key=st.session_state.chave_api)
        st.sidebar.success('Chave API válida', icon='✅')
    else:
        st.sidebar.warning('Informe a chave API', icon='⚠️')

# --- Criar o modelo --- #
modelo = genai.GenerativeModel('gemini-2.0-flash')

# --- Colocar o campo para a entrada do usuário --- #
prompt = st.text_input(
    label='Entrada do usuário',
    placeholder='Pergunte algo sobre a imagem...'
)

# --- Colocar o campo para o envio da imagem --- #
imagem_envio = st.file_uploader(
    label='Escolha uma imagem para enviar',
    type=['jpg', 'jpeg', 'png']
)

# --- Colocar o botão para enviar a imagem ao modelo --- #
enviar = st.button('Enviar')

# --- Criar as colunas para separar a imagem e a resposta --- #
colunas = st.columns(2)

# --- Se a imagem for enviada, abrir e passar para o modelo --- #
with colunas[0]:
    if imagem_envio is not None:
        imagem = Image.open(imagem_envio)
        st.image(imagem, use_container_width=True)

# --- Enviar a imagem com a pergunta ao modelo --- #
if enviar:
    dados_imagem = imagem2bytes(imagem_envio)
    resposta = resposta_gemini(modelo, dados_imagem, prompt)
    with colunas[1]:
        st.subheader('Resposta:')
        st.write(resposta)
