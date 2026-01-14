# --- Importar os módulos do PySide6 --- #
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


class Cronometro:
    """Classe do aplicativo."""
    def __init__(self):
        """Função que inicializa a classe."""
        # --- Carregador da interface --- #
        carregador = QUiLoader()

        # --- Carregar a interface --- #
        self.ui = carregador.load('./interface/interface.ui')

        # --- Título do aplicativo --- #
        self.ui.setWindowTitle('Cronômetro')
        
        # --- Ícone do aplicativo --- #
        self.ui.setWindowIcon(QIcon('./interface/imagem/icone.png'))


if __name__ == '__main__':
    app = QApplication()
    cronometro = Cronometro()
    cronometro.ui.show()
    app.exec()
