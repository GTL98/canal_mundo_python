# --- Importar o Streamlit --- #
import streamlit as st

# --- Configurações iniciais da página --- #
st.set_page_config(
    page_title='Aula 05 - Estado da Sessão',
    layout='wide'
)

# --- Inicializar o estado da sessão --- #
if 'logado' not in st.session_state:
    st.session_state.logado = False

if 'usuario' not in st.session_state:
    st.session_state.usuario = ''

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}

if 'etapa' not in st.session_state:
    st.session_state.etapa = 'login'


# --- Definição de callbacks com suporte a args e kwargs --- #
def adicionar_produto(nome_produto, preco, quantidade=1):
    """Função de callback para inserir e acumular itens no carrinho."""
    if nome_produto in st.session_state.carrinho:
        st.session_state.carrinho[nome_produto]['quantidade'] += quantidade
    else:
        st.session_state.carrinho[nome_produto] = {'preco': preco, 'quantidade': quantidade}


# --- Título da página --- #
st.title('Sistema de Gestão de Estados')

# --- Navegação básica e sincronização via parâmetro key --- #
if st.session_state.etapa == 'login':
    st.subheader('Autenticação do Usuário')
    # --- O st.text_input() é vinculado diretamente ao st.session_state --- #
    st.text_input(
        label='Nome do operador:',
        placeholder='Digite o seu nome',
        key='temp_usuario'
    )

    if st.button('Acessar Sistema', type='primary'):
        # --- Recuperação direta do valor sem precisar de variáveis globais --- #
        if st.session_state.temp_usuario.strip():
            st.session_state.usuario = st.session_state.temp_usuario.strip()
            st.session_state.logado = True
            st.session_state.etapa = 'catalogo'
            st.rerun()
        else:
            st.warning('Insira um nome válido para prosseguir.')

elif st.session_state.etapa == 'catalogo':
    st.subheader('Catálogo de Produtos')
    st.write(f'Bem-vindo ao terminal operacional, {st.session_state.usuario}')

    # --- Catálogo disponível --- #
    produtos_disponiveis = {
        'Notebook Gamer': 5200.00,
        'Monitor Ultrawide': 1890.00
    }

    # --- Trabalhar com os dados --- #
    for produto, preco in produtos_disponiveis.items():
        colunas = st.columns(3)
        colunas[0].write(f'**{produto}** - R$ {preco:,.2f}')

        # --- Chave única para obter a quantidade do widget --- #
        chave_limpa = f'input_quantidade_{produto.replace(" ", "_")}'
        colunas[1].number_input(
            label='Quantidade:',
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=chave_limpa
        )

        # --- Executar o callback passando os argumentos pocisionais e nomeados --- #
        colunas[2].button(
            label=f'Adicionar {produto}',
            key=f'botao_adicionar_{produto.replace(" ", "_")}',
            on_click=adicionar_produto,
            args=(produto, preco),
            kwargs={'quantidade': st.session_state.get(chave_limpa, 1)}
        )

    st.divider()
    st.write(f'Estado atual do carrinho: {st.session_state.carrinho}')

    if st.button('Sair'):
        st.session_state.etapa = 'login'
        st.session_state.logado = False
        st.session_state.carrinho = {}
        st.rerun()
