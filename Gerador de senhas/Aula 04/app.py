# --- Importar os módulos do PySide2 --- #
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon, QFont, QFontDatabase

# --- Importar os módulos para a geração da senha aleatória --- #
import string
from random import sample

# --- Importar os recursos --- #
from interface.recursos import recursos


class GeradorSenha:
    """Classe do aplicativo."""
    def __init__(self):
        """Função de inicialização da classe."""
        # --- Carregador da GUI --- #
        carregador = QUiLoader()

        # --- Carregar a GUI --- #
        self.ui = carregador.load('./interface/interface.ui')

        # --- Título do aplicativo --- #
        self.ui.setWindowTitle('Gerador de senha')

        # --- Colocar o ícone do aplicativo --- #
        self.ui.setWindowIcon(QIcon('./interface/imagens/icone.png'))

        # --- Configurar a fonte --- #
        fonte_id = QFontDatabase.addApplicationFont('./interface/fonte/Montserrat-Medium.ttf')
        fonte_familia = QFontDatabase.applicationFontFamilies(fonte_id)
        fonte = QFont(fonte_familia[0], 14)

        # --- Fonte do título --- #
        fonte_titulo = QFont(fonte_familia[0], 24)
        fonte_titulo.setBold(True)
        self.ui.label_titulo.setFont(fonte_titulo)

        # --- Fonte da label da senha --- #
        fonte.setBold(True)
        self.ui.label_senha.setFont(fonte)

        # --- Fonte do campo da senha --- #
        fonte.setBold(False)
        self.ui.linha_senha.setFont(fonte)

        # --- Fonte do botão --- #
        fonte.setBold(False)
        self.ui.botao_gerar.setFont(fonte)

        # --- Fonte da label do slider --- #
        fonte.setBold(True)
        self.ui.label_slider.setFont(fonte)

        # --- Fonte da quantidade de caracteres --- #
        fonte.setBold(True)
        self.ui.label_comprimento.setFont(fonte)

        # --- Fonte do grupo de escolha dos caracteres --- #
        fonte.setBold(True)
        self.ui.groupbox_caracteres.setFont(fonte)

        # --- Fonte do botão de copiar --- #
        fonte.setBold(False)
        self.ui.botao_copiar.setFont(fonte)

        # --- Tamanho máximo e mínimo do slider --- #
        self.ui.slider_comprimento.setMinimum(6)
        self.ui.slider_comprimento.setMaximum(32)

        # --- Mostrar o valor inicial do slider --- #
        self.ui.label_comprimento.setText(str(self.ui.slider_comprimento.value()))

        # --- Mostrar o valor do slider --- #
        self.ui.slider_comprimento.valueChanged.connect(self.atualizar_slider)

        # --- Gerar a senha ao clicar no botão --- #
        self.ui.botao_gerar.clicked.connect(self.gerar_senha)

        # --- Copiar a senha ao clicar no botão --- #
        self.ui.botao_copiar.clicked.connect(self.copiar)

    def atualizar_slider(self):
        """Função responsável por atualizar o valor do slider."""
        # --- Mostrar o valor do slider atualizado --- #
        valor = self.ui.slider_comprimento.value()
        self.ui.label_comprimento.setText(str(valor))

    def gerar_senha(self):
        """Função responsável por gerar a senha aleatória."""
        # --- Comprimento da senha --- #
        comprimento = self.ui.slider_comprimento.value()

        # --- Caracteres da senha --- #
        caracteres = ''

        # --- Verificar qual caixa de seleção foi selecionada --- #
        if self.ui.checkbox_minusculas.isChecked():
            caracteres += string.ascii_lowercase
        if self.ui.checkbox_maiusculas.isChecked():
            caracteres += string.ascii_uppercase
        if self.ui.checkbox_numeros.isChecked():
            caracteres += string.digits
        if self.ui.checkbox_especiais.isChecked():
            caracteres += string.punctuation

        # --- Verificar o tamanho da senha --- #
        if len(caracteres) < comprimento:
            self.ui.linha_senha.setText('Erro: Qtde. de caracteres insuficiente.')
        if not caracteres:
            self.ui.linha_senha.setText('Erro: Nenhum caractere informado.')

        # --- Colocar os caracteres no campo --- #
        senha = ''.join(sample(caracteres, comprimento))
        self.ui.linha_senha.setText(senha)

        # --- Permitir que seja somente de leitura o campo da senha --- #
        self.ui.linha_senha.setReadOnly(True)

    def copiar(self):
        """Função responsável por copiar a senha gerada."""
        # --- Obter a senha --- #
        senha = self.ui.linha_senha.text()

        # --- Copiador --- #
        copiador = QApplication.clipboard()

        # --- Indicar qual texto será copiado --- #
        copiador.setText(senha)


if __name__ == '__main__':
    app = QApplication()
    gerador = GeradorSenha()
    gerador.ui.show()
    app.exec_()
