# --- Importar os módulos --- #
from random import choice
from kivymd.app import MDApp
from kivy.lang import Builder


class Aula04App(MDApp):
    def build(self):
        # --- Título do app --- #
        self.title = 'Motor de Temas - Paleta de Cores'

        # --- Tema --- #
        self.theme_cls.theme_style = 'Light'

        # --- Paleta primária incial --- #
        self.theme_cls.primary_palette = 'Indigo'

        # --- Tom da paleta primária --- #
        self.theme_cls.primary_hue = '500'

        # --- Paleta de acento --- #
        self.theme_cls.accent_palette = 'Amber'

        # --- Carregamento da interface --- #
        return Builder.load_file('./interface.kv')

    def alterar_paleta(self):
        # --- Lista de paletas --- #
        lista_paletas = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo',
                         'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
                         'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange',
                         'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        # --- Aplicação da nova paleta de cor primária --- #
        self.theme_cls.primary_palette = choice(lista_paletas)

    def alterar_tonalidade_primaria(self):
        # --- Escala de tons de opaciadade --- #
        lista_tonalidades = ['50', '100', '200', '300', '400',
                             '500', '600', '700', '800', '900',
                             'A100', 'A200', 'A400', 'A700']

        # --- Aplicar o novo tom --- #
        self.theme_cls.primary_hue = choice(lista_tonalidades)
        self.theme_cls.property('primary_palette').dispatch(self.theme_cls)

    def alterar_acento(self):
        # --- Lista de acentos do KivyMD --- #
        lista_acentos = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo',
                         'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
                         'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange',
                         'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        # --- Aplicação da nova paleta de acento --- #
        self.theme_cls.accent_palette = choice(lista_acentos)

    def resetar_tema(self):
        # --- Resetar para o tema original --- #
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_palette = 'Amber'


if __name__ == '__main__':
    Aula04App().run()