# --- Importar os módulos --- #
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QCheckBox, QRadioButton, QButtonGroup, QMessageBox)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIntValidator


class InteracoesWidgets(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Configurações da janela principal --- #
        self.setWindowTitle('Aula 3: Domínio de Widgets e Entrada de Dados')
        self.setMinimumSize(500, 600)

        # --- Widget central e layout principal --- #
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        self.layout_principal = QVBoxLayout(self.widget_central)
        self.layout_principal.setSpacing(15)
        self.layout_principal.setContentsMargins(20, 20, 20, 20)

        # --- Inicializar a função --- #
        self.configurar_interface()

    def configurar_interface(self):
        # --- Título com QLabel --- #
        self.label_titulo = QLabel('Cadastro de Perfil de Desenvelvedor')

        # --- Aplicar estilos via QSS para melhorar o visual --- #
        self.label_titulo.setStyleSheet('''
        font-size: 20px;
        font-weight: bold;
        color: #ACBF19;
        margin-bottom: 10px
        ''')
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_principal.addWidget(self.label_titulo)

        # --- Descrição com suporte a quebra de linha --- #
        self.label_descricao = QLabel('Bem-vindo! Este formulário demonstra o uso de widgets '
                                      'para coleta de dados e interação em tempo real.')
        self.label_descricao.setWordWrap(True)  # essencial para textos longos
        self.layout_principal.addWidget(self.label_descricao)

        # --- Campos de entrada com QLineEdit --- #
        self.layout_principal.addWidget(QLabel('Nome de usuário:'))
        self.nome_entrada = QLineEdit()
        self.nome_entrada.setPlaceholderText('Digite seu nome completo...')
        self.nome_entrada.setClearButtonEnabled(True)  # botão para limpar o campo
        self.layout_principal.addWidget(self.nome_entrada)

        self.layout_principal.addWidget(QLabel('Código de acesso (números 1000-9999):'))
        self.codigo_entrada = QLineEdit()
        self.codigo_entrada.setPlaceholderText('Ex: 1234')
        validador_int = QIntValidator(1000, 9999, self)
        self.codigo_entrada.setValidator(validador_int)
        self.layout_principal.addWidget(self.codigo_entrada)

        self.layout_principal.addWidget(QLabel('Senha do sistema:'))
        self.senha_entrada = QLineEdit()
        self.senha_entrada.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout_principal.addWidget(self.senha_entrada)

        # --- Seleção explusiva com QRadioButton e QButtonGroup --- #
        self.layout_principal.addWidget(QLabel('Linguagem de programação principal:'))

        # --- Layout horizontal para os botões de seleção exclusiva --- #
        self.layout_radio = QHBoxLayout()
        self.rb_python = QRadioButton('Python')
        self.rb_cpp = QRadioButton('C++')
        self.rb_java = QRadioButton('Java')

        # --- Criar o grupo lógico para gerenciar a exclusividade --- #
        self.grupo_linguagens = QButtonGroup(self)
        self.grupo_linguagens.addButton(self.rb_python, 1)  # ID 1
        self.grupo_linguagens.addButton(self.rb_cpp, 2)  # ID 2
        self.grupo_linguagens.addButton(self.rb_java, 3)  # ID 3

        # --- Deixar um radio button selecionado --- #
        self.rb_python.setChecked(True)

        self.layout_radio.addWidget(self.rb_python)
        self.layout_radio.addWidget(self.rb_cpp)
        self.layout_radio.addWidget(self.rb_java)
        self.layout_principal.addLayout(self.layout_radio)

        # --- Opções com QCheckBox --- #
        self.layout_principal.addWidget(QLabel('Preferências de notificação:'))
        self.check_email = QCheckBox('Receber atualizações por e-mail')
        self.check_sms = QCheckBox('Receber alerta por SMS')
        self.check_email.setChecked(True)  # deixar marcado como padrão

        self.layout_principal.addWidget(self.check_email)
        self.layout_principal.addWidget(self.check_sms)

        # --- Exemplo de checkbox tri-state (três estado) --- #
        self.check_termos = QCheckBox('Aceito os termos e condições')
        self.check_termos.setTristate(True)
        self.layout_principal.addWidget(self.check_termos)

        # --- Botão de comando QPushButton --- #
        self.botao_processar = QPushButton('Processar cadastro')
        self.botao_processar.setMinimumHeight(40)
        self.botao_processar.setStyleSheet('''
                QPushButton {
                    background-color: #3498DB;
                    color: white;
                    border-radius: 5px;
                    font-weight: bold
                }
                QPushButton:hover {background-color: #2980B9}
                QPushButton:pressed {background-color: #1A5276}
                ''')

        # --- Conexão do sinal clicked() ao Slot personalizado --- #
        self.botao_processar.clicked.connect(self.processar_dados)
        self.layout_principal.addWidget(self.botao_processar)

    @Slot()  # "conversa" entre o PySide6 e C++
    def processar_dados(self):
        # --- Lógica de extração e validação simples --- #
        nome = self.nome_entrada.text()
        codigo = self.codigo_entrada.text()
        email = self.check_email.isChecked()
        sms = self.check_sms.isChecked()
        python = self.rb_python.isChecked()
        cpp = self.rb_cpp.isChecked()
        java = self.rb_java.isChecked()

        if not nome or not codigo:
            QMessageBox.warning(self, 'Erro de Validação',
                                'Por favor, preencha o nome e código de acesso!')
            return
        if email:
            receber_email = 'Sim'
        if not email:
            receber_email = 'Não'
        if sms:
            receber_sms = 'Sim'
        if not sms:
            receber_sms ='Não'
        if python:
            linguagem = 'Python'
        if cpp:
            linguagem = 'C++'
        if java:
            linguagem = 'Java'

        resumo = f'''Cadastro realizado!
Desenvolvedor: {nome}
Código: {codigo}
Receber e-mail: {receber_email}
Receber SMS: {receber_sms}
Linguagem: {linguagem}'''
        QMessageBox.information(self, 'Sucesso', resumo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = InteracoesWidgets()
    janela.show()
    sys.exit(app.exec())