# --- Importar o Steamlit --- #
import streamlit as st

# --- Título da página --- #
st.title('Elementos Interativos de Layout')

# --- Barra lateral --- #
st.sidebar.header('Opções da aplicação')
nome = st.sidebar.text_input(label='Digite o seu nome')
st.sidebar.write(f'Olá, {nome}!')

# --- Colunas para organizar o conteúdo principal --- #
colunas = st.columns(2)

with colunas[0]:
    st.header('Interações simples')
    if st.button('Me aperte!'):
        st.success('Você clicou no botão!')

    valor_slider = st.slider(
        label='Selecione um valor',
        min_value=0,
        max_value=100,
        value=50
    )
    st.write(f'O valor selecionado no slider é: {valor_slider}')

with colunas[1]:
    st.header('Informações e imagens')
    st.info('Esta é uma mensagem informativa')

    # --- Você pode usar uma URL de imagem ou um caminho de um arquivo local --- #
    st.image(
        image='https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-lighttext.png',
        caption='Logo do Streamlit',
        use_container_width=True
    )
    st.warning('Atenção: Este é um aviso')

# --- Entrada de número e exibição --- #
numero = st.number_input(
    label='Digite um número',
    min_value=0,
    max_value=100
)
st.write(f'Você digitou o número: {numero}')
