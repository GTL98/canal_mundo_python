# --- Importar os módulos do Kivy --- #
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, NumericProperty

# --- Carregar o arquivo KV --- #
Builder.load_file('./senha.kv')


class LayoutGeradorSenha(BoxLayout):
    """Classe responsável pela criação do layout do app."""
    # --- Configurar as propriedades dos widgets --- #
    maiusculas = BooleanProperty(True)
    minusculas = BooleanProperty(True)
    numeros = BooleanProperty(True)
    especiais = BooleanProperty(False)
    tamanho_senha = NumericProperty(12)

    def atualizar_tamanho(self, valor):
        """Função responsável por atualizar o valor da senha."""
        self.tamanho_senha = int(valor)


class GeradorSenhaApp(App):
    """Classe responsável pela criação do app."""
    def build(self):
        """Função responsável por gerar o app."""
        return LayoutGeradorSenha()


# --- Inicializar o app --- #
if __name__ == '__main__':
    GeradorSenhaApp().run()
