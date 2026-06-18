# --- Importar as bibliotecas --- #
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.text import LabelBase


class Aula05App(MDApp):
    def build(self):
        # --- Configuração do esquema de cores e estilo visual global --- #
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Indigo'

        # --- Adicionar a fonte --- #
        dir_fontes = 'fontes'
        dir_fonte_nome = 'AdventPro'
        caminho_fonte = os.path.join(dir_fontes, dir_fonte_nome)
        if os.path.exists(caminho_fonte):
            regular = 'AdventPro-Regular.ttf'
            negrito = 'AdventPro-Bold.ttf'
            italico = 'AdventPro-Italic.ttf'
            LabelBase.register(
                name='AdventPro',
                fn_regular=os.path.join(caminho_fonte, regular),
                fn_bold=os.path.join(caminho_fonte, negrito),
                fn_italic=os.path.join(caminho_fonte, italico)
            )
        else:
            LabelBase.register(
                name='AdventPro',
                fn_regular='Roboto'
            )

        # --- Injeção do novo estilo tipográfico no motor do KivyMD --- #
        self.theme_cls.font_styles['AdventPro'] = [
            'AdventPro',  # mesmo nome em LabelBase.register()
            24,  # tamanho da fonte
            False,  # mantém minúsculas e maiúsculas
            0.15  # espaçamento entre as letras
        ]

        # --- Carregar o arquivo da KVLang --- #
        return Builder.load_file('./interface.kv')


if __name__ == '__main__':
    Aula05App().run()
