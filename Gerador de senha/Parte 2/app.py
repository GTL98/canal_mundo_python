# --- Importar os módulos para a criação da GUI --- #
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

# --- Importar o módulo criado para gerar as senhas --- #
from gerador_senhas import gerador_senha


class GeradorSenha:
    """Classe que gera o app."""
    def __init__(self):
        """Função responsável por inicializar a classe."""
        # --- Carregador do arquivo da GUI --- #
        carregador = QUiLoader()

        # --- Carregar o arquivo da GUI --- #
        self.ui = carregador.load('./interface_grafica/interface_grafica_senha.ui')

        # --- Mudar o título do app --- #
        self.ui.setWindowTitle('Gerador de senha')

        # --- Colocar o ícone no app --- #
        self.ui.setWindowIcon(QIcon('./interface_grafica/icone.png'))

        # --- Botão que gera a senha --- #
        self.ui.botao_gerar_senha.clicked.connect(self.gerar_senha)

    def gerar_senha(self):
        """Função responsável por gerar a senha aleatória."""
        # --- Obter a quantidade de caracteres da senha --- #
        quantidade = int(self.ui.linha_quantidade_caracteres.text())

        # --- Criar a senha --- #
        senha = gerador_senha(quantidade)

        # --- Colocar a senha no campo indicado --- #
        campo_senha = self.ui.linha_senha_aleatoria
        campo_senha.setText(senha)
        campo_senha.setReadOnly(True)


if __name__ == '__main__':
    app = QApplication()
    interface = GeradorSenha()
    interface.ui.show()
    app.exec_()
