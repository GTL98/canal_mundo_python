# --- Importar as bibliotecas --- #
import time
import sqlite3
import numpy as np
import pandas as pd
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Performance e Caching Pro',
    page_icon='⚡',
    layout='wide'
)

# --- Título da página --- #
st.title('Aula 03: Estratégias de Caching: Data vs Resource')


# --- Demonstração de st.cache_data --- #
@st.cache_data(show_spinner='Processando base de dados...')
def carregar_transformar_dados(linhas=50_000):
    """
    Simula uma operação de carga e limpeza de dados pesada.
    Utilizamos st.cache_data porque o retorno é um objeto serializável (DataFrame).
    """
    # --- Simular a latência de processamento ou E/S --- #
    time.sleep(3)

    # --- Criar os dados --- #
    dados = pd.DataFrame(
        np.random.randn(linhas, 4),
        columns=['col_1', 'col_2', 'col_3', 'col_4']
    )

    # --- Simular a transformação de dados --- #
    dados = dados.apply(lambda x: x * 100)

    return dados


st.header('Otimização de Dados com st.cache_data')

# --- Interface para disparar a carga de dados --- #
linhas = st.slider(
    label='Quantidade de linhas para processar:',
    min_value=5_000,
    max_value=100_000,
    step=5_000,
    value=50_000
)

t_i = time.time()
df = carregar_transformar_dados(linhas)
t_f = time.time()

st.success(f'Operação concluída em {t_f - t_i:.2f} segundos!')
st.dataframe(df)
st.divider()

# --- Gerenciameno de memória e expiração --- #
st.header('Controle de Expiração e Limites de Memória')


@st.cache_data(ttl='10s', max_entries=20)
def obter_metricas_api(categoria):
    """
    Simula a busca de métricas em uma API externa que muda periodicamente.
    O parâmetro ttl (Time-To-Live) garante que os dados não fiquem obsoletos.
    O parâmetro max_entries evita o estouro de memória (OOM).
    """
    # --- Simular a chamada de uma API --- #
    st.toast(f'Consultando API para categoria: {categoria}')
    time.sleep(1.5)

    metricas = {
        'categoria': categoria,
        'timestamp': time.ctime(),
        'valor': np.random.uniform(100, 1000)
    }

    return metricas


# --- Seleção de categoria para testar o cache com TTL --- #
api_cat = st.radio(
    label='Selecione a categoria da métrica',
    options=['Visitas', 'Vendas', 'Devoluções'],
    horizontal=True
)

if st.button('Buscar métricas'):
    metricas = obter_metricas_api(api_cat)
    st.write('Dados recuperados da API (ou cache):')
    st.json(metricas)
    st.info('Este dado será mantido em cache por no máximo 10 segundos (TTL)')
st.divider()

st.header('Persistência de Recursos com st.cache_resource')


@st.cache_resource
def obter_engine_banco_dados():
    """
    Inicializa um motor de conexão SQL.
    Usamos st.cache_resource pois a conexão não é serializável.
    Este objeto será compartilhado entre TODOS os usuários da aplicação.
    """
    st.warning('⚙️ Inicializando o Motor do Banco de Dados (Recurso Global)...')

    # --- Simulação de inicialização de um recurso pesado (banco de dados ou modelo de ML) --- #
    time.sleep(2)

    # --- Criar uma conexão SQLite em memória --- #
    conn = sqlite3.connect(':memory:', check_same_thread=True)

    return conn


# --- Inicializar o recurso --- #
bd_engine = obter_engine_banco_dados()

st.write('O motor de banco de dados está pronto e em memória.')
st.caption('Recursos cacheados via st.cache_resource agem como Singletons e não são copiados.')
st.divider()

st.header('Hashing Avançado e o "Escape Hatch" (_parametro)')


@st.cache_data(show_spinner='Realizando query complexa...')
def query_otimizada(_engine, query_id, usuario='Usuário'):
    """
    Executa uma query no banco de dados.
    O parâmetro _engine começa com sublinhado para ser IGNORADO pelo hasher.
    O cache será indexado apenas pelo query_id e usuario.
    """
    st.write(f'🔍 Buscando dados no BD para o ID: {query_id}')
    time.sleep(2)

    # --- Simular o resultado --- #
    return pd.DataFrame({
        'id': [query_id],
        'usuario': [usuario],
        'acesso': [time.ctime()]
    })


# --- Controle de entrada para query --- #
query_id = st.number_input(
    label='ID do resgitro:',
    min_value=1,
    max_value=999,
    value=10
)
usuario = st.selectbox(
    label='Nível de acesso:',
    options=['Admin', 'Usuário', 'Editor']
)

if st.button('Executar consulta'):
    # --- Passar o objeto de conexão bd_engine, que é unhashable --- #
    resultado_query = query_otimizada(bd_engine, query_id, usuario)
    st.table(resultado_query)
    st.success('Query executada com sucesso utilizando o escape hatch de hashing!')