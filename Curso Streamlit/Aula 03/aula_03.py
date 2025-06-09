# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import streamlit as st

# --- Título da página --- #
st.title('Trabalhando com Dados e Gráficos')

# --- Cabeçalho --- #
st.header('Gerando e Exibindo Dados Aletórios')

# --- Gerar um DataFrame de exemplo --- #
df = pd.DataFrame(
    np.random.randn(20, 3),  # 20 linhas e 3 colunas de números aleatórios
    columns=['a', 'b', 'c']  # nomes das colunas
)

# --- Exibir o DataFrame de forma interativa --- #
st.subheader('Aqui é um DataFrame gerado aleatoriamente:')
st.dataframe(df)

# --- Exibir os gráficos --- #
st.subheader('Gráficos simples com dados:')
st.line_chart(df)  # gráfico de linha com as colunas do DataFrame
st.bar_chart(df)  # gráfico de barras

# --- Exemplo com upload de arquivo --- #
st.subheader('Carregando dados de um arquivo CSV:')
upload = st.file_uploader(
    label='Escolha um arquivo CSV',
    type='csv'
)

if upload is not None:
    try:
        # --- Mostrar um pedaço do arquivo --- #
        df_upload = pd.read_csv(upload)
        st.success('Arquivo carregado com sucesso!')
        st.write('As primeiras 5 linhas do seu arquivo:')
        st.dataframe(df_upload.head())

        # --- Tentar plotar as duas primeiras colunas, se existirem --- #
        if df_upload.shape[1] >= 2:
            st.subheader('Gráfico das duas primeiras colunas:')
            st.line_chart(df_upload.iloc[:, :2])
        else:
            st.info('Seu arquivo tem menos de 2 colunas')

    except Exception as e:
        st.error(f'Erro ao carregar o arquivo: {e}. Certifique-se de que é um arquivo CSV válido.')
