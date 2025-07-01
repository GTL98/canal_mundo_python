# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

# --- Título da página --- #
st.title('Visualização de Dados Avançada')

# --- Dados de exemplo --- #
df = pd.DataFrame(
    {
        'data': pd.to_datetime(pd.date_range(start='2025-01-01', periods=100)),
        'valor_a': np.random.rand(100).cumsum(),
        'valor_b': np.random.rand(100).cumsum() + 10
    }
)

# --- Matplotlib --- #
st.header('Matplotlib')
fig, ax = plt.subplots()
ax.plot(df['data'], df['valor_a'], label='Valor A')
ax.plot(df['data'], df['valor_b'], label='Valor B')
ax.set_title('Série temporal Matplotlib')
ax.legend()
st.pyplot(fig)

# --- Plotly --- #
st.header('Plotly')
fig_plotly = px.line(
    data_frame=df,
    x='data',
    y=['valor_a', 'valor_b'],
    title='Série temporal Plotly'
)
st.plotly_chart(fig_plotly)

# --- Altair --- #
st.header('Altair')
fig_altair = alt.Chart(df).mark_line().encode(
    x='data',
    y=alt.Y('valor_a', title='Valor A'),
    tooltip=['data', 'valor_a']
).properties(title='Série temporal Altair (Valor A)')
st.altair_chart(fig_altair)