# --- Importar os módulos --- #
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QHBoxLayout, QVBoxLayout, QLabel,
                               QPushButton, QFrame)


class Horizon(QMainWindow):
    def __init__(self):
        # --- Herdar a classe pai --- #
        super().__init__()

        # --- Configurações iniciais do app --- #
        self.setWindowTitle('Sistema Horizon - Gestão de Ativos')
        self.resize(500, 350)

        # --- Instanciar o widget central --- #
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)

        # --- Criar o layout vertical principal --- #
        self.layout_principal = QVBoxLayout()

        # --- Margem externa (distância do layout principal com as margens do app) --- #
        self.layout_principal.setContentsMargins(20, 20, 20, 20)

        # --- Espeço entre os layouts internos (cabeçalho, frame e rodapé) --- #
        self.layout_principal.setSpacing(15)

        self.widget_central.setLayout(self.layout_principal)

        # --- Cabeçalho horizontal --- #
        self.layout_cabecalho = QHBoxLayout()
        self.layout_cabecalho.setSpacing(10)

        self.label_titulo = QLabel('Painel de Controle Horizon')
        self.layout_cabecalho.addWidget(self.label_titulo)

        # --- Adição de uma mola para alinhar o botão --- #
        self.layout_cabecalho.addStretch(1)

        self.botao_status = QPushButton('Status: Ativo')
        self.layout_cabecalho.addWidget(self.botao_status)

        # --- Adicionar o layout do cabeçalho ao layout principal --- #
        self.layout_principal.addLayout(self.layout_cabecalho)

        # --- Área de visualização central --- #
        self.frame_conteudo = QFrame()
        self.frame_conteudo.setFrameShape(QFrame.StyledPanel)
        self.layout_principal.addWidget(self.frame_conteudo)

        # --- Rodapé horizontal com botões --- #
        self.layout_rodape = QHBoxLayout()
        self.layout_rodape.setSpacing(10)

        # --- Empurrar os botões para o canto direito --- #
        self.layout_rodape.addStretch(1)

        self.botao_cancelar = QPushButton('Cancelar')
        self.layout_rodape.addWidget(self.botao_cancelar)

        self.botao_salvar = QPushButton('Salvar Configurações')
        self.layout_rodape.addWidget(self.botao_salvar)

        # --- Adicionar o layout do rodapé ao layout principal --- #
        self.layout_principal.addLayout(self.layout_rodape)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    horizon = Horizon()
    horizon.show()
    sys.exit(app.exec())