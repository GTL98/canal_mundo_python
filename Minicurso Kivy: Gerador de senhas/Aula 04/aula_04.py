# --- Importar os módulos do Kivy --- #
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.properties import BooleanProperty, NumericProperty, StringProperty

# --- Importar as bibliotecas para a geração da senha --- #
import string
import random

# --- Carregar o arquivo KV --- #
Builder.load_file('./senha.kv')


class LayoutGeradorSenha(BoxLayout):
    """Classe responsável pela criação do layout do app."""
    # --- Configurar as propriedades dos widgets --- #
    maiusculas = BooleanProperty(False)
    minusculas = BooleanProperty(False)
    numeros = BooleanProperty(False)
    especiais = BooleanProperty(False)
    tamanho_senha = NumericProperty(12)
    senha_gerada = StringProperty('Sua senha aparecerá aqui')
    mensagem_feedback = StringProperty('')

    def atualizar_tamanho(self, valor):
        """Função responsável por atualizar o valor da senha."""
        self.tamanho_senha = int(valor)

    def gerador_senha(self):
        """Função responsável por gerar a senha aleatória."""
        # --- String com os caracteres selecionados --- #
        caracteres = ''

        # --- Seleção das checkboxes --- #
        if self.maiusculas:
            caracteres += string.ascii_uppercase
        if self.minusculas:
            caracteres += string.ascii_lowercase
        if self.numeros:
            caracteres += string.digits
        if self.especiais:
            caracteres += string.punctuation

        # --- Informar se nenhuma checkbox for selecionada --- #
        if not caracteres:
            self.senha_gerada = 'Selecione ao menos um tipo'
            return

        # --- Selecionar os caracteres para a criação da senha --- #
        self.senha_gerada = ''.join(
            random.choice(caracteres) for _ in range(self.tamanho_senha)
        )

        # --- Copiar a senha --- #
        if self.senha_gerada:
            Clipboard.copy(self.senha_gerada)

        # --- Mensagem de feedback informando da cópia da senha --- #
        self.mensagem_feedback = 'Senha copiada para a área de transferência!'


class GeradorSenhaApp(App):
    """Classe responsável pela criação do app."""
    def build(self):
        """Função responsável por gerar o app."""
        return LayoutGeradorSenha()


# --- Inicializar o app --- #
if __name__ == '__main__':
    GeradorSenhaApp().run()
