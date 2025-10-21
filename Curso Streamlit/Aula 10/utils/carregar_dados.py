# --- Importar as bibliotecas --- #
import pandas as pd
import streamlit as st


@st.cache_data
def carregar_dados():
    """Função responsável por carregar os dados de exemplo para a aplicação."""
    dados = {
        'col_1': [1, 2, 3, 4, 5],
        'col_2': [10, 20, 15, 25, 30],
        'col_3': ['A', 'B', 'A', 'C', 'B']
    }
    return pd.DataFrame(dados)
