# --- Importar as bibliotecas --- #
import time
import random
import streamlit as st
import google.generativeai as genai

# --- Configurações do site --- #
st.set_page_config(
    page_title='Streamlit e Gemini',
    page_icon=':robot:'
)

# --- Título na página --- #
st.title('Streamlit e Gemini 🤖')
st.caption('Chatbox feito com Gemini Pro')

# --- Alocar a chave API no site --- #
if 'chave_api' not in st.session_state:
    chave_api = st.sidebar.text_input('Chave API', type='password')
    if chave_api.startswith('AI'):
        st.session_state.chave_api = chave_api
        genai.configure(api_key=st.session_state.chave_api)
        st.sidebar.success('Chave de API válida!', icon='✅')
    else:
        st.sidebar.warning('Informe a chave de API', icon='⚠️')

# --- Criar o histórico do chat --- #
if 'historico' not in st.session_state:
    st.session_state.historico = []

# --- Criar o modelo --- #
modelo = genai.GenerativeModel('gemini-2.0-flash')

# --- Criar o chat --- #
chat = modelo.start_chat(history=st.session_state.historico)

# --- Colocar um botão na sidebar para limpar o chat --- #
with st.sidebar:
    if st.button('Limpar a conversa', type='primary', use_container_width=True):
        st.session_state.historico = []
        st.rerun()

# --- Obter as mensagens do histórico --- #
for mensagem in chat.history:
    if mensagem.role == 'model':
        role = 'assistant'
    else:
        role = mensagem.role
    with st.chat_message(role):
        st.markdown(mensagem.parts[0].text)

# --- Se a chave API foi informada, criar o chat --- #
if 'chave_api' in st.session_state:
    prompt = st.chat_input('')
    if prompt:
        prompt = prompt.replace('\n', ' \n')
        # --- Escrever a entrada do usuário --- #
        with st.chat_message('user'):
            st.markdown(prompt)
        # --- Escrever a mensagem do Gemini --- #
        with st.chat_message('assistant'):
            mensagem_placeholder = st.empty()
            mensagem_placeholder.markdown('Pensando...')
            # --- Verificar se não há erro na entrada do usuário --- #
            try:
                # --- Escrever a resposta do Gemini letra por letra --- #
                resposta = ''
                for chunk in chat.send_message(prompt, stream=True):
                    contagem_palavras = 0
                    n_aleatorio = random.randint(5, 10)
                    for palavra in chunk.text:
                        resposta += palavra
                        contagem_palavras += 1
                        # --- Escrever a palavra como se fosse uma máquina de escrever --- #
                        if contagem_palavras == n_aleatorio:
                            time.sleep(0.05)
                            mensagem_placeholder.markdown(resposta + '_')
                            contagem_palavras = 0
                            n_aleatorio = random.randint(5, 10)
                mensagem_placeholder.markdown(resposta)
            except genai.types.generation_types.BlockedPromptException as e:
                st.exception(e)
            except Exception as e:
                st.exception(e)
            st.session_state.historico = chat.history
