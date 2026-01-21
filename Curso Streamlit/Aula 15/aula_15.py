# --- Importar as bibliotecas --- #
import pandas as pd
import streamlit as st


# --- Configuração da página --- #
st.set_page_config(layout='wide')

# --- Título na página --- #
st.title('st.data_editor() na prática')

# --- Dados de exemplo --- #
df = pd.DataFrame({
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Preço': [4500.00, 120.00, 250.00, 1100.00],
    'Estoque': [10, 50, 30, 15],
    'Ativo': [True, True, True, False]
})

# --- Criar o editor de dados --- #
df_editado = st.data_editor(
    df,
    use_container_width=True,
    num_rows='dynamic',  # permite adicionar/remover linhas
    column_config={
        'Produto': st.column_config.TextColumn(
            label='Produto',
            help='Nome do produto',
            max_chars=30
        ),
        'Preço': st.column_config.NumberColumn(
            label='Preço (R$)',
            help='Preço do produto',
            min_value=0.0,
            format='R$ %.2f'
        ),
        'Estoque': st.column_config.NumberColumn(
            label='Quantidade em estoque',
            help='Quantidade do produto',
            min_value=0,
            step=1
        ),
        'Ativo': st.column_config.CheckboxColumn(
            label='Produto ativo',
            help='O produto está à venda'
        )
    }
)

# --- Exibir o DataFrame atualizado --- #
st.dataframe(df_editado)

# --- Conversão do DataFrame para CSV --- #
csv = df_editado.to_csv(index=False).encode('utf-8')

# --- Botão para o download do DataFrame atualizado --- #
st.download_button(
    label='Baixar dados editados (CSV)',
    data=csv,
    file_name='dados_editados.csv',
    mime='text/csv'
)