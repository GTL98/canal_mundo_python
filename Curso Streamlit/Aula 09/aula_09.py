# --- Importar as bibliotecas --- #
import sqlite3
import pandas as pd
import streamlit as st


# --- Título do site --- #
st.title('Integração com Banco de Dados e APIs')

# --- Conexão com SQLite --- #
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# --- Criação de tabela e inserção de dados de exemplo --- #
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
    )
''')
cursor.execute('INSERT INTO produtos (nome, preco) VALUES ("Computador", 3500.00)')
cursor.execute('INSERT INTO produtos (nome, preco) VALUES ("Mouse", 150.00)')

# --- Mostrar os dados --- #
st.header('Produtos do Banco de Dados')
query = 'SELECT * FROM produtos'
df_produtos = pd.read_sql_query(query, conn)
st.dataframe(df_produtos)

# --- Fechar a conexão com o SQLite --- #
conn.close()

# --- Exemplo de API --- #
st.header('Dados de uma API Externa')
import requests
try:
    # --- Obter a requisição --- #
    resposta = requests.get('https://jsonplaceholder.typicode.com/posts?_limit=5')
    posts = resposta.json()

    # --- Mostrar as informações no site --- #
    for post in posts:
        st.subheader(post['title'])
        st.write(post['body'])
        st.write('---')
except requests.exceptions.RequestException as e:
    # --- Caso ocorra algum erro de cnoxão, mostrar qual foi o erro --- #
    st.error(f'Erro ao acessar a API: {e}')
