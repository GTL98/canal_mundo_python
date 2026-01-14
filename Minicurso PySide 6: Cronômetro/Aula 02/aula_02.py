# --- Importar os módulos do PySide6 --- #
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
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

        # --- Timer --- #
        self.tempo = 0  # tempo em segundos
        self.timer = QTimer()  # timer do Qt
        self.timer.timeout.connect(self.atualizar_tempo)

        # --- Conectsr os botões às funções --- #
        self.ui.botao_iniciar.clicked.connect(self.iniciar)
        self.ui.botao_pausar.clicked.connect(self.pausar)
        self.ui.botao_resetar.clicked.connect(self.resetar)

        # --- Atualização dos botões --- #
        self.atualizar_botoes(False)

    def iniciar(self):
        """Função responsável por iniciar o cronômetro."""
        # --- Disparar o timer a cada 1 segundo --- #
        self.timer.start(1000)

        # --- Permitir que o botão de iniciar esteja liberado --- #
        self.atualizar_botoes(True)

    def pausar(self):
        """Função responsável por pausar o cronômetro."""
        # --- Parar o cronômetro --- #
        self.timer.stop()

        # ---  botão de pausar é desabilitado por padrão --- #
        self.atualizar_botoes(False)

    def resetar(self):
        """Função responsável por reiniciar o cronômetro."""
        # --- Parar o cronômetro --- #
        self.timer.stop()

        # --- Reiniciar o tempo --- #
        self.tempo = 0

        # --- Reescrever o visor --- #
        self.ui.label_cronometro.setText('00:00')

        # --- Atualizar os botões --- #
        self.atualizar_botoes(False)

    def atualizar_botoes(self, iniciado):
        """Função responsável por habilitar e desabilitar os botões de iniciar e pausar."""
        self.ui.botao_iniciar.setEnabled(not iniciado)
        self.ui.botao_pausar.setEnabled(iniciado)

    def atualizar_tempo(self):
        """Função responsável por atualizar o QTimer."""
        # --- Incrementar o tempo em segundos --- #
        self.tempo += 1

        # --- Obter os minutos --- #
        minutos = self.tempo // 60

        # --- Obter os segundos --- #
        segundos = self.tempo % 60

        # --- Atualizar o visor do cronômetro --- #
        self.ui.label_cronometro.setText(f'{minutos:02d}:{segundos:02d}')


if __name__ == '__main__':
    app = QApplication()
    cronometro = Cronometro()
    cronometro.ui.show()
    app.exec()
