# --- Importar o Streamlit --- #
import streamlit as st

# --- Configurações da página --- #
st.set_page_config(layout='centered')

# --- Título da página --- #
st.title('Aula prática: st.dialog() e st.popover()')

# --- Botão que abre o dialog --- #
if st.button('Abrir diálogo de confirmação'):
    st.session_state.abrir_dialog = True

# --- Criar o dialog --- #
@st.dialog('Confirmação de ação')
def dialog_confirmacao():
    # --- Texto explicativo dentro do dialog --- #
    st.write('Esta ação simula ima decisão importante dentro da aplicação')

    # --- Campo de entrada --- #
    nome = st.text_input('Digite seu nome para confirmar')

    # --- Botões de ação --- #
    colunas = st.columns(2)
    with colunas[0]:
        if st.button('Confirmar'):
            # --- Salvar na sessão o nome --- #
            st.session_state['nome'] = nome
            st.session_state.abrir_dialog = False
            st.rerun()

    with colunas[1]:
        if st.button('Cancelar'):
            st.session_state.abrir_dialog = False
            st.rerun()

# --- Controle para abrir o dialog --- #
if st.session_state.get('abrir_dialog', False):
    dialog_confirmacao()

# --- Colocar o nome na página --- #
if 'nome' in st.session_state:
    st.success(f'Ação confirmada para: {st.session_state.nome}')

st.divider()

# --- Conteúdo principal da página --- #
st.write('Aqui está o conteúdo principal da página')
st.write('As configurações extras ficam ocultas no popover')

# --- Popover para opções secundárias --- #
with st.popover('Abrir opções avançadas'):
    # --- Conteúdo exibido apenas dentro do popover --- #
    st.write('Configurações rápidas')

    # --- Widgets comuns dentro do popover --- #
    tema = st.selectbox(
        label='Escolha um tema',
        options=['Claro', 'Escuro', 'Sistema']
    )
    notificacoes = st.checkbox('Ativar notificações')

    # --- Salvar as escolhas na sessão --- #
    if st.button('Salvar configurações'):
        st.session_state.tema = tema
        st.session_state.notificacoes = notificacoes
        st.success('Configurações salvas')

# --- Exibir as configurações escolhidas --- #
if 'tema' in st.session_state:
    st.info(f'Tema selecionado: {st.session_state.tema}')

if 'notificacoes' in st.session_state:
    st.info(f'Notificações ativas: {st.session_state.notificacoes}')