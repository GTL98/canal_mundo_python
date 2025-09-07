# --- Importar o Streamlit --- #
import streamlit as st

# --- Título da página --- #
st.title('Calculadora Streamlit')

# --- Campo do primeiro número --- #
num_1 = st.number_input(label='Digite o primeiro número', format='%0f')

# --- Campo do segundo número --- #
num_2 = st.number_input(label='Digite o segundo número', format='%0f')

# --- Colunas --- #
colunas = st.columns(4)

# --- Botão de soma --- #
with colunas[0]:
    if st.button(label='Soma', use_container_width=True):
        resultado = num_1 + num_2
        st.write(f'O resultado é: {resultado}')

# --- Botão de subtração --- #
with colunas[1]:
    if st.button(label='Subtração', use_container_width=True):
        resultado = num_1 - num_2
        st.write(f'O resultado é: {resultado}')

# --- Botão de multiplicação --- #
with colunas[2]:
    if st.button(label='Multiplicação', use_container_width=True):
        resultado = num_1 * num_2
        st.write(f'O resultado é: {resultado}')

# --- Botão de divisão --- #
with colunas[3]:
    if st.button(label='Divisão', use_container_width=True):
        resultado = num_1 / num_2
        st.write(f'O resultado é: {resultado}')
