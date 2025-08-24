# --- Importar as bibliotecas --- #
import time
import streamlit as st

# --- Configurações da página --- #
st.set_page_config(
    page_title='Customização do App',
    page_icon='✨',
    layout='wide'
)

# --- Título da página --- #
st.title('Customização e Componentes')

# --- Explicação do site --- #
st.markdown("""
Esta aplicação demonstra a tematização e a ideia de componentes customizados.
As cores e fontes que você vê agora são definidas no arquivo `.streamlit/config.toml`
""")

# --- Exemplo de st.status --- #
st.header('Mensagem de status')
with st.status('Preparando dados...', expanded=True) as status:
    st.write('Buscando dados da fonte...')
    time.sleep(2)
    st.write('Processando informações...')
    time.sleep(1)
    st.write('Gerando relatório final...')
    status.update(label='Dados carregados!', state='complete')
st.success('Processo concluído!')