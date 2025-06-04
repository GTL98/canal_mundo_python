# --- Importar as dependências Kivy --- #
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class GeradorSenha(BoxLayout):
    """Representa o widget principal do gerador de senhas."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = [20, 20, 20, 20]

        # --- Campo da senha gerada referenciada no KV --- #
        self.saida_senha = None

    def gerar_senha(self):
        """Função placeholder para gerar a senha."""
        self.ids.saida_senha.text = 'SenhaGerada123!'


# --- Carregar o arquivo KV --- #
Builder.load_file('./gerador_senha.kv')


class GeradorSenhaApp(App):
    """
    Esta é a classe principal do aplicativo Kivy.
    Ela carrega o arquivo KV e retorna a instância do widget raiz.
    """
    def build(self):
        # --- Definir a cor de fundo da tela --- #
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        # --- Retornar a instância do nosso widget principal, que será construído com base no KV --- #
        return GeradorSenha()


if __name__ == '__main__':
    GeradorSenhaApp().run()
