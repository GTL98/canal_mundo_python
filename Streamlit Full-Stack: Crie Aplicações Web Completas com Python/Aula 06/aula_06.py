# --- Importar as bibliotecas --- #
import pytz
import streamlit as st
from datetime import datetime

# --- Configuração da página --- #
st.set_page_config(
    page_title='Aula 06',
    layout='wide'
)


# --- Função de callback para redefinir as variáveis de modo seguro --- #
def redefinir_filtros():
    # --- Atualização direta do session_state sincronizado aos widgets --- #
    st.session_state.curso = 'Ciência de Dados'
    st.session_state.vagas = 30


# --- Título da aula --- #
st.title('Aula 06: Widget Binding e Sinconização de URL')

# --- Caixa de seleção vinculada à URL --- #
curso = st.selectbox(
    label='Selecione o curso de interesse:',
    options=sorted([
        'Engenharia de Dados',
        'Ciência de Dados',
        'Inteligência Artificial'
    ]),
    key='curso',
    bind='query-params'
)

# --- Entrada numética vinculada à URL --- #
vagas = st.number_input(
    label='Quantidade máxima de vagas:',
    min_value=5,
    max_value=100,
    value=30,
    key='vagas',
    bind='query-params'
)

# --- Capturar os metadados do usuário --- #
fuso_horario = st.context.timezone or 'UTC'
idioma = st.context.locale or 'pt-BR'
ip = st.context.ip_address

# --- Determinar o horário local no fuso horário do usuário --- #
try:
    time_zone = pytz.timezone(fuso_horario)
    hora_local = datetime.now(pytz.utc).astimezone(time_zone).strftime('%H:%M:%S')
except Exception:
    hora_local = datetime.now().strftime('%H:%M:%S')

# --- Botãp de redefinição --- #
st.button(
    label='Redefinir filtros',
    on_click=redefinir_filtros,
    width='stretch'
)

# --- Mostrar as entradas do usuário --- #
st.write(f'Curso atualmente selecionado: **{curso}** | Limite de **{vagas}** vagas')
st.write(f'Fuso horário: **{fuso_horario}** (Hora local: {hora_local}) | Idiioma: **{idioma}** '
         f'| IP: **{ip}**')