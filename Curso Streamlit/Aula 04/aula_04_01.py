# --- Importar o Streamlit --- #
import streamlit as st

# --- Título da página --- #
st.title('Contador e Estado da Sessão')

# --- Inicializar o session_state se ainda não existir --- #
if 'contador' not in st.session_state:
    st.session_state.contador = 0

def incrementar_contador():
    st.session_state.contador += 1

# --- Mostrar o valor atual do contador --- #
st.write(f'O valor atual do contador é: {st.session_state.contador}')

# --- Aumentar o valor do contador --- #
st.button(
    label='Incrementar',
    on_click=incrementar_contador
)

# --- Exemplo de formulário que mantém o estado --- #
st.header('Formulário com estado')
if 'nome_usuario' not in st.session_state:
    st.session_state.nome_usuario = ''

def atualizar_nome():
    st.session_state.nome_usuario = st.session_state.nome_usuario_input

st.text_input(
    label='Digite o seu nome:',
    key='nome_usuario_input',
    on_change=atualizar_nome
)

st.write(f'Nome salvo: {st.session_state.nome_usuario}')
