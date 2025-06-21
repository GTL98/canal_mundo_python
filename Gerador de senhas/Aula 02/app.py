# --- Importar os módulos do PySide2 --- #
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon, QFont, QFontDatabase

# --- Importar os módulos para a geração da senha aleatória --- #
import string
from random import sample


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
        self.ui.setWindowIcon(QIcon('./interface/icone.png'))

        # --- Configurar a fonte --- #
        fonte_id = QFontDatabase.addApplicationFont('./interface/Montserrat-Medium.ttf')
        fonte_familia = QFontDatabase.applicationFontFamilies(fonte_id)

        # --- Fonte do título --- #
        fonte_titulo = QFont(fonte_familia[0], 24)
        fonte_titulo.setBold(True)
        self.ui.label_titulo.setFont(fonte_titulo)

        # --- Fonte da label da senha --- #
        fonte_label_senha = QFont(fonte_familia[0], 14)
        fonte_label_senha.setBold(True)
        self.ui.label_senha.setFont(fonte_label_senha)

        # --- Fonte do campo da senha --- #
        fonte_senha = QFont(fonte_familia[0], 14)
        self.ui.linha_senha.setFont(fonte_senha)

        # --- Fonte do botão --- #
        fonte_botao = QFont(fonte_familia[0], 14)
        self.ui.botao_gerar.setFont(fonte_botao)

        # --- Gerar a senha ao clicar no botão --- #
        self.ui.botao_gerar.clicked.connect(self.gerar_senha)

    def gerar_senha(self):
        """Função responsável por gerar a senha aleatória."""
        # --- Comprimento da senha --- #
        comprimento = 12

        # --- Caracteres da senha --- #
        caracteres = (
            string.digits +
            string.punctuation +
            string.ascii_lowercase +
            string.ascii_uppercase
        )

        # --- Colocar os caracteres no campo --- #
        senha = ''.join(sample(caracteres, comprimento))
        self.ui.linha_senha.setText(senha)

        # --- Permitir que seja somente de leitura o campo da senha --- #
        self.ui.linha_senha.setReadOnly(True)


if __name__ == '__main__':
    app = QApplication()
    gerador = GeradorSenha()
    gerador.ui.show()
    app.exec_()
