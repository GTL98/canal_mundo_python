# --- Importar os módulos --- #
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

# --- Configuração do tamanho da tela --- #
Window.size = (360, 640)


class Aula1(MDApp):
    def build(self):
        """Este método será o responsável por retornar a estrutura da interface."""
        # --- Definir o título do app --- #
        self.title = 'Curso de KivyMD: Aula 01'

        # --- Acessar o ThemeManager para configurar a identidade visual --- #
        self.theme_cls.theme_style = 'Dark'  # mudança para o modo escuro
        self.theme_cls.accent_palette = 'Amber'  # cor de destaque
        self.theme_cls.primary_palette = 'Indigo'  # paleta de cor principal

        # --- Criação de um MDScreen fornece a base para os widgets do Material Desing --- #
        self.tela_principal = MDScreen()

        # --- O MDLabel reage automaticamente ao modo Dark (escuro) --- #
        self.texto_central = MDLabel(
            text='Explorando o MDApp',
            halign='center',
            font_style='H4',
            theme_text_color='Primary'
        )

        # --- Adicionar a label como widget filho da tela principal --- #
        self.tela_principal.add_widget(self.texto_central)

        # --- O retorno deste widget define a raiz da aplicação --- #
        return self.tela_principal

    def on_start(self):
        """Disparado com a UI está pronta e visível."""
        print('A aplicação iniciou com sucesso!')
        self.texto_central.text = 'Bem-vindo ao MDApp!'
        
        # --- Ativar o modo FPS nativo do KivyMD para depuração --- #
        self.fps_monitor_start()

    def on_pause(self):
        """Disparado quando o app vai para segundo plano."""
        print('Aplicação em segundo plano...')
        return True

    def on_resume(self):
        """Disparado quando o usuário volta para o aplicativo."""
        print('Aplicação restaurada!')
        self.texto_central.text = 'Bem-vindo de volta!'

    def on_stop(self):
        """Disparado no fechamento total da aplicação."""
        print('Evento: App encerrado. Limpando memória...')


if __name__ == '__main__':
    # --- Instanciação da classe e execução do loop principal --- #
    Aula1().run()
