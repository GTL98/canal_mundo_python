# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

# --- Configuração da página do site --- #
st.set_page_config(layout='wide')

# --- Título da página --- #
st.title('st.metric() na prática')

# --- Criar um conjunto de dados fictícios --- #
np.random.seed(42)

dados = pd.DataFrame({
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'vendas_atual': np.random.randint(8000, 15000, 6),
    'vendas_anterior': np.random.randint(7000, 14000, 6)
})

# --- Cálculo das métricas principais --- #
total_vendas_atual = dados['vendas_atual'].sum()
total_vendas_anterior = dados['vendas_anterior'].sum()
delta_vendas = total_vendas_atual - total_vendas_anterior
percental_variacao = (delta_vendas / total_vendas_anterior) * 100

# --- Colocar as métricas no site --- #
colunas = st.columns(3)

with colunas[0]:
    st.metric(
        label='Vendas Totais',
        value=f'R$ {total_vendas_atual:,.2f}',
        delta=f'R$ {delta_vendas:,.2f}'
    )

with colunas[1]:
    st.metric(
        label='Variação (%)',
        value=f'{percental_variacao:.2f}%',
        delta=f'{percental_variacao:.2f}%'
    )

media_mensal = dados['vendas_atual'].mean()
media_mensal_anterior = dados['vendas_anterior'].mean()
delta_media = media_mensal - media_mensal_anterior

with colunas[2]:
    st.metric(
        label='Média Mensal',
        value=f'R$ {media_mensal_anterior:,.2f}',
        delta=f'R$ {delta_media:,.2f}'
    )

# --- Selecionar quais dados serão lidos na métrica --- #
st.divider()
st.subheader('Métricas dinâmicas')

mes_selecionado = st.selectbox(
    label='Selecione um mês',
    options=dados['mes']
)

linha_mes = dados[dados['mes'] == mes_selecionado].iloc[0]

vendas_atual_mes = linha_mes['vendas_atual']
vendas_anterior_mes = linha_mes['vendas_anterior']
delta_mes = vendas_atual_mes - vendas_anterior_mes
delta_formatado = ''
if delta_mes < 0:
    delta_formatado = f'-R$ {delta_mes:,.2f}'
else:
    delta_formatado = f'R$ {delta_mes:,.2f}'

st.metric(
    label=f'Vendas em {mes_selecionado}',
    value=f'R$ {vendas_atual_mes:,.2f}',
    delta=delta_formatado
)

# --- Colocar gráficos junto com as métricas --- #
st.divider()
st.subheader('st.metric() com gráficos embutidos')

# --- Gerador de números aleatórios --- #
gerador = rng(4)

# --- Variação dos dados --- #
mudancas = list(gerador.standard_normal(20))

# --- Série acumulada da evolução do indicador --- #
dados = [sum(mudancas[:i]) for i in range(20)]

# --- Delta --- #
delta = round(dados[-1], 2)

# --- Colocar as métricas com os gráficos --- #
colunas = st.columns(3)

with colunas[0]:
    st.metric(
        label='Indicador (linha)',
        value=10,
        delta=delta,
        chart_data=dados,
        chart_type='line',
        border=True
    )

with colunas[1]:
    st.metric(
        label='Indicador (área)',
        value=10,
        delta=delta,
        chart_data=dados,
        chart_type='area',
        border=True
    )

with colunas[2]:
    st.metric(
        label='Indicador (barra)',
        value=10,
        delta=delta,
        chart_data=dados,
        chart_type='bar',
        border=True
    )