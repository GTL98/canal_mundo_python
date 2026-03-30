# --- Importar os módulos --- #
import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel,
                               QMenuBar, QToolBar, QStatusBar)


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Configurações fundamentais da janela principal --- #
        self.setWindowTitle('Sistema Profissional PySide6')
        self.resize(1024, 768)

        # --- Criação e configuração do widget central --- #
        self.widget_central = QLabel('Área de trabalho principal')
        self.widget_central.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_central.setStyleSheet('''
        QLabel {
            font-size: 20pt;
            color: #34495e;
            background-color: #ecf0f1;
            border: 5px dashed #bdc3c7;
            border-radius: 10px;
            margin: 20px
            }
        ''')

        # --- Definição obrigatória do widget central no QMainWindow --- #
        self.setCentralWidget(self.widget_central)

        # --- Definição de ações compartilhadas (QAction) --- #
        self.acao_novo = QAction(QIcon.fromTheme('document-new'), '&Novo Arquivo', self)
        self.acao_novo.setShortcut(QKeySequence.StandardKey.New)
        self.acao_novo.setStatusTip('Criar um novo arquivo em branco')
        self.acao_novo.triggered.connect(self.slot_novo_arquivo)

        self.acao_abrir = QAction('&Abrir...', self)
        self.acao_abrir.setShortcut(QKeySequence.StandardKey.Open)
        self.acao_abrir.setStatusTip('Abrir um arquivo existente')

        self.acao_sair = QAction('&Sair', self)
        self.acao_sair.setShortcut('Ctrl+Q')
        self.acao_sair.setStatusTip('Fechar o sistema com segurança')
        self.acao_sair.triggered.connect(self.close)

        # --- Acesso à barra de menus da janela --- #
        menu = self.menuBar()

        # --- Criação de menus principais --- #
        menu_arquivo = menu.addMenu('&Arquivo')
        menu_editar = menu.addMenu('&Editar')

        # --- Adição de ações ao menu Arquivo --- #
        menu_arquivo.addAction(self.acao_novo)
        menu_arquivo.addAction(self.acao_abrir)
        menu_arquivo.addSeparator()  # linha visual de divisória
        menu_arquivo.addAction(self.acao_sair)

        # --- Criação da barra de ferramentas --- #
        self.toolbar = QToolBar('Barra principal')
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        # --- Reutilização das mesmas ações para garantir consistência --- #
        self.toolbar.addAction(self.acao_novo)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.acao_sair)

        # --- Customização do estilo da toolbar --- #
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        # --- Inicialização da barra de status --- #
        self.status = self.statusBar()

        # --- Exibição de uma mensagem temporária de inicialização --- #
        self.status.showMessage('Sistema Horizon pronto para operação', 5000)  # dura 5 segundos

        # --- Adição de um widget permanente --- #
        self.label_versao = QLabel('Versão 1.2.0 | Engine: PySide6 v6.10')
        self.status.addPermanentWidget(self.label_versao)

    def slot_novo_arquivo(self):
        """Resposta à ação de criar um novo arquivo."""
        self.widget_central.setText('Ação "Novo Arquivo" executada!')
        self.status.showMessage('Novo arquivo criado.', 3000)


if __name__ == '__main__':
    # --- Inicalização da infraestrutura do Qt --- #
    app = QApplication()

    # --- Instanciação da interface principal --- #
    janela = JanelaPrincipal()
    janela.show()

    # --- Início do loop de eventos --- #
    sys.exit(app.exec())