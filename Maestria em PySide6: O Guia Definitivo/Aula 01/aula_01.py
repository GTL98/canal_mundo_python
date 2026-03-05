# --- Importar as bibliotecas --- #
import sys
from PySide6.QtWidgets import QApplication, QLabel


def aula_01():
    # --- QApplication deve ser a primeira coisa a ser criada --- #
    app = QApplication(sys.argv)

    # --- Configurações dos metadados --- #
    app.setApplicationName('Aula 01')
    app.setApplicationVersion('0.0.1')
    app.setOrganizationName('Mundo Python')
    app.setOrganizationDomain('https://www.youtube.com/@Mundo_Python')

    # --- Criar uma Label --- #
    # --- O QLabel é um widget que exibe texto ou imagens --- #
    janela = QLabel('''Aula 01: O ciclo de vida da QApplication.
O framework está ativo e aguardando eventos.''')
    janela.setWindowTitle('Aula 01 de PySide6')
    janela.resize(480, 320)
    janela.setMinimumSize(400, 200)

    # --- O método show() é necessário para mostrar os widgets que são invisíveis por padrão --- #
    janela.show()

    # --- sys.exit interrompe o interpretador Python e retorna o código do Qt --- #
    # --- Isso é fundamental para que scripts externos saibam se o app fechou OK --- #
    sys.exit(app.exec())

if __name__ == '__main__':
    aula_01()