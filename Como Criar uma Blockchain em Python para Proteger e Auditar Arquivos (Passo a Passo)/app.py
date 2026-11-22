# --- Importar os módulos --- #
import streamlit as st
from curadoria import SistemaCuradoria

# --- Instanciar o sistema de curadoria --- #
sistema = SistemaCuradoria()

# --- Configurações da página --- #
st.set_page_config(
    page_title='Curadoria arquivos Blockchain',
    layout='wide'
)

# --- Título na página --- #
st.title('Curadoria de arquivos')

# --- Criar as abas --- #
abas = st.tabs(['Registrar', 'Histórico', 'Auditoria'], on_change='rerun')

# --- Aba de registro --- #
with abas[0]:
    if abas[0].open:
        st.header('Registre o seu documento')
        id_documento = st.text_input('Informe o ID do documento:')
        nome_arquivo = st.text_input('Informe o nome do documento com a extensão:')
        curador = st.text_input('Informe o nome do curador do documento:')
        versao = st.number_input('Informe a versão do documento:', step=1, min_value=0)
        observacao = st.text_area('Informe alguma observação do documento se houver:')
        status = st.radio(
            label='Informe o status do documento:',
            options=['Revisão', 'Aprovado', 'Rejeitado'],
            horizontal=True
        )
        documento = st.file_uploader('Selecione o seu documento:')
        if st.button('Registrar', width='stretch'):
            sistema.registrar_documento(
                id_documento=id_documento,
                nome_arquivo=nome_arquivo,
                conteudo_bytes=documento.getvalue(),
                curador=curador,
                versao=versao,
                status=status,
                observacao=observacao
            )
            st.success(f'Documento {nome_arquivo} ({id_documento}) registrado na Blockchain.')

# --- Aba do histórico --- #
with abas[1]:
    if abas[1].open:
        st.header('Veja o histórico do documento')
        documentos = sistema.listar_ids_documentos()
        id_documento = st.selectbox(
            label='Selecione o ID do documento:',
            options=documentos,
            index=None,
            placeholder='Escolha uma opção'
        )

        if id_documento is not None:
            historico = sistema.obter_historico_documento(id_documento)
            validacao, mensagem, conteudo = sistema.obter_arquivo_seguro(historico)
            if validacao:
                st.success(mensagem)
                st.download_button(
                    label='Baixar',
                    data=conteudo,
                    file_name='arquivo.txt',
                    mime='txt',
                    on_click='ignore',
                    width='stretch'
                )
            else:
                st.error(mensagem)

# --- Aba de auditoria --- #
with abas[2]:
    if abas[2].open:
        st.header('Auditoria do documento')
        documento = st.file_uploader('Selecione o documento:')
        if documento is not None:
            audicao = sistema.auditar_arquivo_externo(documento.getvalue())
            if audicao['valido']:
                st.success(f'{audicao["motivo"]}')
                st.subheader(f'ID documento: {audicao["detalhes"]["id_documento"]}')
                st.subheader(f'Nome original: {audicao["detalhes"]["nome_original"]}')
                st.subheader(f'Versão: {audicao["detalhes"]["versao"]}')
                st.subheader(f'Curador: {audicao["detalhes"]["curador"]}')
                st.subheader(f'Observação: {audicao["detalhes"]["observacao"]}')
                st.subheader(f'Status: {audicao["detalhes"]["status"]}')
                st.subheader(f'Data registro: {audicao["detalhes"]["data_registro"]}')
            else:
                st.warning(f'{audicao["motivo"]}')
