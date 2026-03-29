# --- Importar os módulos --- #
import os
from kivymd.app import MDApp
from kivy.lang import Builder


class Aula02App(MDApp):
    def build(self):
        # --- O método build() deve retornar o widget raiz da aplicação --- #
        # --- Configurações globais de tema que afeta os widgets declarados --- #
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.accent_palette = 'Amber'

        # --- Builder.load_file() carrega o arquivo KV e instancia os objetos --- #
        caminho_kv = os.path.join(os.path.dirname(__file__), 'interface.kv')
        return Builder.load_file(caminho_kv)

    def validar_registro(self, nome, projeto):
        """Lógica de negócios que interage com a interface declarativa via IDs"""
        if nome.strip() and projeto.strip():
            # --- Acesso direto aos widgets do KV através do dicionário self.root.ids --- #
            self.root.ids.feedback_final.text = f'Sucesso! Projeto {projeto} registrado para {nome}.'
            self.root.ids.feedback_final.theme_text_color = 'Primary'
            print(f'Log: Registro validado para {nome} em {projeto}')
        else:
            self.root.ids.feedback_final.text = 'Erro: Preencha todos os campos obrigatórios.'
            self.root.ids.feedback_final.theme_text_color = 'Error'

    def reiniciar_campos(self):
        """Reseta o estado da interface para os valores padrão."""
        self.root.ids.input_nome.text = ''
        self.root.ids.input_projeto.text = ''
        self.root.ids.feedback_final.text = 'Formulário reiniciado. Aguardando novos dados.'
        self.root.ids.feedback_final.theme_text_color = 'Secondary'


if __name__ == '__main__':
    Aula02App().run()