# --- Importar os módulos --- #
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# --- Tamanho da tela --- #
Window.size = (360, 640)


class Aula03App(MDApp):
    def build(self):
        # --- Configurações iniciais do objeto theme_cls --- #
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.theme_style = 'Light'

        # --- Ativar a animação de transição entre os temas --- #
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5

        # --- Carregar a interface gráfica --- #
        return Builder.load_file('./interface.kv')

    def atualizar_tema(self, instancia_switch, estado_ativado):
        """
        Método chamado pelo evento on_active do MDSwitch no arquivo KV.
        Altera o theme_style global do aplicativo.
        """
        if estado_ativado:
            # --- Se o switch estiver ativo, mudamos para o modo escuro --- #
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Teal'
        else:
            # --- Caso contrário, é retornado ao modo claro --- #
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.primary_palette = 'Indigo'

        print(f'''Estilo do tema: {self.theme_cls.theme_style}
Paleta primária atual: {self.theme_cls.primary_palette}''')


if __name__ == '__main__':
    Aula03App().run()