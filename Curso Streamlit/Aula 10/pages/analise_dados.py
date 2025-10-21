# --- Importar as bibliotecas --- #
import streamlit as st
import plotly.express as px

# --- Importar o módulo de carregamento de dados --- #
from utils.carregar_dados import carregar_dados


def analise_dados():
    """Função responsável por analisar e mostrar os dados."""
    st.title('Página de Análise de Dados')
    st.write('Aqui você pode visualizar e analisar os dados.')

    # --- Carregar os dados --- #
    df = carregar_dados()
    st.subheader('Dados carregados:')
    st.dataframe(df)

    # --- Mostrar o gráfico --- #
    st.subheader('Gráfico da Análise:')
    fig = px.bar(df, x='col_3', y='col_2', title='Soma de Col. 2 por Col. 3')
    st.plotly_chart(fig)
