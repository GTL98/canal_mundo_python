# --- Importar os módulos --- #
import sys
import pygame

# --- Importar as configurações --- #
from config import *

# --- Importar o módulo do jogador --- #
from jogador import Jogador


class DoodleJump:
    def __init__(self):
        # --- Inicializar o Pygame --- #
        pygame.init()

        # --- Configurar a tela do jogo --- #
        self.TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption('Python Doodle Jump')

        # --- Controlador de FPS --- #
        self.relogio = pygame.time.Clock()

        # --- Flag de execução do jogo --- #
        self.rodando = True

        # --- Instanciar o jogador --- #
        self.jogador = Jogador()

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
        # --- Movimentar o jogador --- #
        self.jogador.mover()

    def desenhar(self):
        # --- Desenhar na tela --- #
        self.TELA.fill(BRANCO)
        self.jogador.desenhar(self.TELA)
        pygame.display.flip()

    def rodar(self):
        # --- Executar o jogo --- #
        while self.rodando:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)

        # --- Fechar a tela quando fechar o jogo --- #
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    jogo = DoodleJump()
    jogo.rodar()