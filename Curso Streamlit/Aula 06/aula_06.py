# --- Importar os módulos --- #
import streamlit as st
from datetime import date, time

# --- Título da página --- #
st.title('Widgets Avançados de Entrada')

st.header('Seleção de opções')

# --- Caixa de seleção --- #
opcao_selecionada = st.selectbox(
    label='Qual a sua fruta favorita?',
    options=(
        'Maçã',
        'Banana',
        'Laranja',
        'Uva'
    )
)
st.write(f'Você selecionou: {opcao_selecionada}')

# --- Multiseleção --- #
multiplas_opcoes = st.multiselect(
    label='Quais frutas você gosta?',
    options=[
        'Maçã',
        'Banana',
        'Laranja',
        'Uva',
        'Morango',
        'Abacaxi'
    ],
    placeholder='Selecione as frutas'
)
st.write(f'Você gosta de: {", ".join(multiplas_opcoes) if multiplas_opcoes else "Nenhuma"}')

# --- Radio button --- #
genero = st.radio(
    label='Qual o seu gênero?',
    options=(
        'Masculino',
        'Feminino',
        'Outro'
    )
)
st.write(f'Gênero selecionado: {genero}')

st.header('Seleção de data e hora')

# --- Selecionar a data --- #
data = st.date_input(
    label='Selecione uma data:',
    value=date.today()
)
st.write(f'Data selecionada: {data}')

# --- Selecionar a hora --- #
hora = st.time_input(
    label='Selecione uma hora:',
    value=time(20, 30)
)
st.write(f'Hora selecionada: {hora}')

st.header('Checkbox e download')

# --- Caixa de seleção e botão de download --- #
termos = st.checkbox('Eu aceito os termos e condições.')
if termos:
    st.success('Termos aceitos!')
    st.download_button(
        label='Baixar relatório',
        data='Conteúdo do relatório de exemplo.',
        file_name='relatorio_exemplo.txt',
        mime='text/plain'
    )
else:
    st.info('Por favor, aceite os termos.')

st.header('Formulários com st.form()')

# --- Formulário (os widgets ficam todos juntos) --- #
with st.form('meu_formulario_contado'):
    st.write('Preencha os seus dados:')
    nome = st.text_input('Nome:')
    email = st.text_input('E-mail:')
    mensagem = st.text_area('Mensagem:')
    submissao = st.form_submit_button('Enviar mensagem')

    if submissao:
        if nome and email and mensagem:
            st.success(f'Mensagem de {nome} enviada com sucesso!')
            st.write(f'E-mail: {email}')
            st.write(f'Mensagem: {mensagem}')
        else:
            st.error('Por favor, preencha todos os campos do formulário.')