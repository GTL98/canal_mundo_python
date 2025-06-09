# --- Importar as bibliotecas --- #
import pandas as pd
import streamlit as st

# --- Título da página --- #
st.title('Retorno da Empresa')

# --- Campo para enviar o arquivo --- #
upload = st.file_uploader(
    label='Envie o arquivo CSV',
    type='csv'
)

# --- Verificar se o arquivo foi enviado --- #
if upload is not None:
    try:
        # --- Mostrar um pedaço do arquivo --- #
        df = pd.read_csv(upload)
        st.success('Arquivo carregado com sucesso!')
        st.write('As 5 primeiras entradas do arquivo:')
        st.dataframe(df.head())

        # --- Plotar o gráfico de linha dos investimentos --- #
        st.subheader('Investimento por meio de comunicação')
        df_investimento = df[['TV', 'Radio', 'Newspaper']]
        st.line_chart(df_investimento)

        # --- Plotar o grádico de barras do retorno --- #
        st.subheader('Retorno')
        df_retorno = df['Sales']
        st.bar_chart(df_retorno)

    except Exception as e:
        st.error(f'Erro ao carregar o arquivo: {e}. Certifique-se de que é um arquivo CSV válido.')
