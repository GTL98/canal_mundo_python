# --- Importar as bibliotecas --- #
import time
import numpy as np
import streamlit as st
from datetime import datetime

# --- Configurações iniciais do site --- #
st.set_page_config(
    page_title='Painel SIGC',
    layout='wide'
)

# --- Título da página --- #
st.title('Sistema Inteligente de Gestão de Crise (SIGC)')
st.markdown('Esta aplicação demonstra o poder de renderização rápida utilizando **Fragmento** em áreas '
            'de alta latência.')

# --- Inicializar os estados da sessão --- #
if 'contador_global' not in st.session_state:
    st.session_state.contador_global = 0
if 'registro_alertas' not in st.session_state:
    st.session_state.registro_alertas = []

# --- Simulação de carregamento de dados históricos (muitos dados) --- #
st.subheader('Visualização de dados históricos')
with st.spinner('Carregando banco de dados de incidentes históricos...'):
    time.sleep(2)
    st.success('Dados históricos carregados com sucesso!')

# --- Atualização e exibição das estatísticas de execução do script principal --- #
st.session_state.contador_global += 1
st.write(f'O script principal rodou {st.session_state.contador_global} vezes')

# --- Widget de entrada --- #
observacoes = st.text_input('Notas do operador (qualquer alteração causará a reexecução total do site):')
if observacoes:
    st.info(f'Nota registrada: {observacoes}')

# --- Adição do fragmento para o monitoramento em tempo real --- #
st.divider()
st.subheader('Monitoramento de sensores em tempo real')

# --- Definição segura do placeholder para logs de segurança --- #
placeholder_alertas = st.sidebar.empty()


# --- Fragmento com atualização contínua e assíncrona de tempos em tempos --- #
@st.fragment(run_every=3)
def monitor_sensores(container_externo):
    # --- Geração de leitura aleatória simulando o sinal de um sensor --- #
    valor_sensor = np.random.randint(85, 110)
    st.metric(
        label='Status do senssor de temperatura',
        value=f'{valor_sensor} °C'
    )

    # --- Validação de anomalias com persistência de estado para compartilhamento de dados --- #
    if valor_sensor > 95:
        timestamp = datetime.now().strftime('%H:%M:%S')
        st.session_state.registro_alertas.insert(0, f'[{timestamp}] Alerta: Temperatura crítica ({valor_sensor} °C)')

    # --- Renderização das últimas entradas do sensor (log na barra lateral) --- #
    with container_externo.container():
        st.subheader('Histórico de alertas:')
        if st.session_state.registro_alertas:
            # --- Exibe apenas os 5 registros --- #
            for alerta in st.session_state.registro_alertas[:5]:
                st.error(alerta)
        else:
            st.info('Nenhum alerta registrado até o momento')

    # --- Widget interativo local que executa apenas as instruções deste fragmento --- #
    if st.button('Forçar atualização local'):
        st.toast('Leitura local atualizada')

    # --- Controle de fluxo: acionamento de parada de segurança e reexecução global automática --- #
    if len(st.session_state.registro_alertas) >= 5:
        st.warning('Limite crítico de segurança atingido. Reiniciando a telemetria global em instantes...')
        time.sleep(2)
        st.session_state.registro_alertas = []
        st.rerun()  # executa a reexecução do script principal para redefinir as conexões


# --- Ativação e renderização da função --- #
monitor_sensores(placeholder_alertas)