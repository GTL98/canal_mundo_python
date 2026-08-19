# --- Importar os módulos --- #
import sys
import pygame

# --- Importar as configurações --- #
from config import *

# --- Importar as classes --- #
from jogador import Jogador
from plataforma import Plataforma


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

        # --- Criar o chão --- #
        self.chao = Plataforma(0, ALTURA_TELA - 20, LARGURA_TELA, 20)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
        # --- Movimentar o jogador --- #
        self.jogador.mover()

        # --- Lógica de colisão com o chão --- #
        # --- Só quica se o jogador estiver caindo (velocidade_y > 0) --- #
        if self.jogador.velocidade_y > 0:
            if self.jogador.rect.colliderect(self.chao.rect):
                self.jogador.velocidade_y = FORCA_PULO

    def desenhar(self):
        # --- Desenhar na tela --- #
        self.TELA.fill(BRANCO)

        # --- Desenhar os objetos do jogo --- #
        self.chao.desenhar(self.TELA)
        self.jogador.desenhar(self.TELA)

        # --- Atualizar a tela --- #
        pygame.display.flip()

    def rodar(self):
        # --- Exutar o jogo --- #
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