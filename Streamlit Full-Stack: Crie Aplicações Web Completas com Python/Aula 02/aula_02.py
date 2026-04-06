# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import streamlit as st

# --- Configuração inicial da página para permitir a estruturação espacial completa --- #
st.set_page_config(
    page_title='Aula 02: Layouts',
    layout='wide'
)

# --- Título da página --- #
st.title('🚀 Aula 02: Estruturação Espacial')
st.markdown('''Nesta aula, contruiremos um dashboard moduloar. O código evuluirá em cada seção,
adicionando camadas de complexidade até termos uma aplicação **completa** e *funcional*.''')

# --- Base de dados para utilizarmos nas visualizações --- #
dados = pd.DataFrame(
    np.random.randn(20, 5),
    columns=['Vendas', 'Lucro', 'Meta', 'Custo', 'Retorno']
)

st.header('O poder das colunas e alinhamento vertical')

# --- Criar colunas com pesos/tamanhos diferentes --- #
colunas = st.columns(
    spec=[1, 3, 1],
    gap='medium',  # controla o espaçemento entre as colunas
    vertical_alignment='center',  # garante que os widgets fiquem visualmente equilibrados
    border=True  # adicionar borda às colunas
)

# --- Adicionar as informações nas colunas --- #
with colunas[0]:
    st.subheader('Indicadores')
    st.metric(
        label='Vendas totais',
        value='R$ 1.250,00',
        delta='12%'
    )
    st.metric(
        label='Lucro líquido',
        value='R$ 450,00',
        delta='-3%'
    )
with colunas[1]:
    st.subheader('Análise visual')
    st.line_chart(dados)
with colunas[2]:
    st.subheader('Ações')
    st.button('Atualizar dados', key='atualizar_dados', use_container_width=True)
    st.button('Exportar PDF', key='exportar_pdf', use_container_width=True)
    st.checkbox('Habilitar modo noturno', key='modo_norturno')
st.divider()

st.header('Containers dinâmicos e layout horizontal')

# --- Criar um container que se comporta como uma barra de ferramentas --- #
st.write('Configurações da seção:')
barra_ferramentas = st.container(
    horizontal=True,  # alinha os elementos internamente em linha
    border=True,
    width='content',  # o container ocupa apenas o espaço necessário
    horizontal_alignment='left'
)

# --- Colocar o container --- #
with barra_ferramentas:
    st.toggle('Filtrar finais de semana', key='filtro_fim_semana')
    st.toggle('Mostrar médias', key='mostrar_medias')
    st.segmented_control(
        label='Escala',
        options=['Diário', 'Semanal', 'Mensal'],
        default='Diário'
    )

# --- Container para exibição de status, utilizando a largura total padrão (stretch) --- #
with st.container(border=True):
    st.info('Esse container demonstra como o conteúdo adapta-se à largura total disponível.')
    st.write('Este bloco pode conter qualquer tipo de widget, como tabelas ou textos longos.')
st.divider()

st.header('Profundidade de interface com abas reativas')

# --- Criar abas que rastreiam seu estado através de uma chave (key) --- #
abas = st.tabs(
    tabs=['Visualização', 'Dados brutos', 'Configurações'],
    on_change='rerun',  # habilita a propriedade .open em cada aba
    key='navegacao_principal'
)

# --- Adicionar informações às abas --- #
with abas[0]:
    # --- A propriedade .open permite executar a lógica condicional de alta performance --- #
    if abas[0].open:
        st.write('Renderizando visualização complexa sob demanda...')
        colunas = st.columns(2, gap='large')
        with colunas[0]:
            st.bar_chart(dados['Vendas'])
        with colunas[1]:
            st.area_chart(dados['Lucro'])
with abas[1]:
    if abas[1].open:
        st.write('Exibindo dados brutos da operação:')
        st.dataframe(dados.style.highlight_max(axis=0), width='stretch')
with abas[2]:
    if abas[2].open:
        st.write('Painel de controle do administrador')
        st.slider('Ajustar limite de alerta', 0, 100, 50)
st.divider()

st.header('Revelação progressiva e popovers')

# --- Criar um popover para filtros avançados que não precisam ocupar espaço fixo --- #
# --- O popover fluta sobre o conteúdo, ideal para menus de configuração --- #
with st.popover('🔍 Filtros avançados e explicações', icon='🛠️'):
    st.write('Use os campos abaixo para refinar sua análise:')
    st.date_input('Filtrar por período', value=None)
    st.multiselect('Selecionar regiões', options=['Norte', 'Sul', 'Leste', 'Oeste'])

    # --- Podemos aninhar em estruturas simples para organização interna --- #
    with st.expander('Ver glossário de termos:'):
        st.caption('Vendas: Valor bruto faturado no período.')
        st.caption('Lucro: Valor líquido após deduções operacionais.')

# --- Exemplo de st.expander() que reage à abertura --- #
def abrir_detalhes():
    st.toast('Você está visualizando os detalhes técnicos', icon='👀')

with st.expander('📄 Detalhes da auditoria (clique para ver)', on_change=abrir_detalhes):
    st.write(f'Timestamp da última atualização: {pd.Timestamp.now()}')