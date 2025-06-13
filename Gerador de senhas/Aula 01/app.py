# --- Importar os módulos do PySide2 --- #
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


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


if __name__ == '__main__':
    app = QApplication()
    gerador = GeradorSenha()
    gerador.ui.show()
    app.exec_()
