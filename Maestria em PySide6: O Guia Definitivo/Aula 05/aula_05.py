# --- Importar os módulos --- #
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication,
                               QComboBox,
                               QFrame,
                               QGridLayout,
                               QLabel,
                               QLineEdit,
                               QPushButton,
                               QTextEdit,
                               QWidget)


class Horizon(QWidget):
    def __init__(self):
        # --- Herdar a classe pai --- #
        super().__init__()

        # --- Configurações iniciais das propriedades da janela --- #
        self.setWindowTitle('Horizon - Gestão de Ativos')
        self.resize(900, 500)

        # --- Inicialização do gerenciador de layout de grade matricial --- #
        self.layout_principal = QGridLayout()
        self.setLayout(self.layout_principal)

        # --- Instanciação dos componentes básicos do formulário --- #
        self.label_nome = QLabel('Nome do ativo:')
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText('Ex: Petrobras PN')

        # --- Adicionar os widgets ao layout principal --- #
        self.layout_principal.addWidget(self.label_nome, 0, 0)  # (widget, linha, coluna)
        self.layout_principal.addWidget(self.input_nome, 0, 1)

        # --- Outros campos --- #
        self.label_tipo = QLabel('Tipo do ativo:')
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems([
            'Ações',
            'FIIs',
            'Renda Extra',
            'Criptomoedas'
        ])

        self.label_preco = QLabel('Preço de aquisição')
        self.input_preco = QLineEdit()
        self.input_preco.setPlaceholderText('0.00')

        # --- Inserção dos novos widgets --- #
        self.layout_principal.addWidget(self.label_tipo, 1, 0)
        self.layout_principal.addWidget(self.combo_tipo, 1, 1)
        self.layout_principal.addWidget(self.label_preco, 2, 0)
        self.layout_principal.addWidget(self.input_preco, 2, 1)

        # --- Campo de observações --- #
        self.label_observacoes = QLabel('Observações:')
        self.input_observacoes = QTextEdit()
        self.input_observacoes.setPlaceholderText('Teste de investimento, metas e riscos...')

        # --- Inserção do campo de observação --- #
        self.layout_principal.addWidget(self.label_observacoes, 3, 0, Qt.AlignmentFlag.AlignTop)
        self.layout_principal.addWidget(self.input_observacoes, 3, 1)

        # --- Painel lateral de monitoramento --- #
        self.painel_estatisticas = QFrame()
        self.painel_estatisticas.setFrameShape(QFrame.Shape.StyledPanel)
        self.painel_estatisticas.setStyleSheet('''
        background-color: #2E3440;
        border-radius: 8px;
        color: #D8DEE9
        ''')

        # --- Configuração do layout interno do painel lateral --- #
        layout_painel = QGridLayout(self.painel_estatisticas)
        self.label_painel = QLabel('Painel Analítico')
        self.label_painel.setStyleSheet('''
        font-weight: bold;
        font-size: 14px;
        color: #88C0D0
        ''')

        self.label_dados_painel = QLabel(
            'Ticker: PETR4\n'
            'Preço de Mercado: R$ 36,15\n'
            'Preço Justo (Grah.): R$ 42,50\n'
            'Margem de Segurança: +17,5%\n'
            'Status: Sobrecomprado'
        )
        self.label_dados_painel.setStyleSheet('''
        font-size: 20px;
        line-height: 1.6;
        color: #E5E9F0
        ''')

        layout_painel.addWidget(self.label_painel, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_painel.addWidget(self.label_dados_painel, 1, 0, Qt.AlignmentFlag.AlignCenter)

        # --- Adição do painel --- #
        self.layout_principal.addWidget(self.painel_estatisticas, 0, 2, 5, 1)  # (widget, linha, coluna, quantas linhas ocupa, quantas colunas ocupa)

        # --- Adição de botões --- #
        self.botao_cancelar = QPushButton('Cancelar')
        self.botao_cancelar.setFixedWidth(100)

        self.botao_salvar = QPushButton('Salvar ativo')
        self.botao_salvar.setFixedWidth(120)

        # --- Adição dos botões com alinhamentos específicos --- #
        self.layout_principal.addWidget(self.botao_cancelar, 4, 0, Qt.AlignmentFlag.AlignLeft)
        self.layout_principal.addWidget(self.botao_salvar, 4, 1, Qt.AlignmentFlag.AlignRight)

        # --- Mergens periféricas ao redor de todo o layout (esquera, topo, direita, base) --- #
        self.layout_principal.setContentsMargins(20, 20, 20, 20)

        # --- Espaçamento entre colunas e linhas vizinhas --- #
        self.layout_principal.setHorizontalSpacing(15)
        self.layout_principal.setVerticalSpacing(12)

        # --- Distribuição de esticamento horizontal (colunas) --- #
        self.layout_principal.setColumnStretch(0, 1)  # menor largura para as labels
        self.layout_principal.setColumnStretch(1, 3)  # largura média para os campos de entrada
        self.layout_principal.setColumnStretch(2, 4)  # maior largura disponível para o painel

        # --- Distribuição de fatores de esticamento vertical (linhas) --- #
        self.layout_principal.setRowStretch(0, 1)
        self.layout_principal.setRowStretch(1, 1)
        self.layout_principal.setRowStretch(2, 1)
        self.layout_principal.setRowStretch(3, 4)  # linha das observações ganha maior relevância
        self.layout_principal.setRowStretch(4, 1)

        # --- Definição de largura mínima para a coluna das labels --- #
        self.layout_principal.setColumnMinimumWidth(0, 110)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    horizon = Horizon()
    horizon.show()
    sys.exit(app.exec())