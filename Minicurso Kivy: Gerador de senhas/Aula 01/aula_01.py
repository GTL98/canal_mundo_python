# --- Importar os módulos do Kivy --- #
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# --- Carregar o arquivo KV --- #
Builder.load_file('./senha.kv')


class LayoutGeradorSenha(BoxLayout):
    """Classe responsável pela criação do layout do app."""
    pass


class GeradorSenhaApp(App):
    """Classe responsável pela criação do app."""
    def build(self):
        """Função responsável por gerar o app."""
        return LayoutGeradorSenha()


# --- Inicializar o app --- #
if __name__ == '__main__':
    GeradorSenhaApp().run()
