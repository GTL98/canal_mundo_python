# --- Importar as bibliotecas --- #
import sys
import pygame

# --- Importar o módulo das configurações --- #
from configuracoes import *

# --- Importar os módulos dos sprites --- #
from bola import Bola
from raquete import Raquete

# --- Importar o módulo do HUD --- #
from hud import HUD


class Pong:
    """Classe responsável pelo jogo."""
    def __init__(self, multiplayer: bool):
        """Função responsável por inicializar a classe."""
        # --- Inicializar o Pygame --- #
        pygame.init()

        # --- Se é multiplayer ou não --- #
        self.multiplayer = multiplayer

        # --- Tela do jogo --- #
        self.TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

        # --- Definir o título da tela --- #
        pygame.display.set_caption('Pong')

        # --- Limitar o FPS --- #
        self.clock = pygame.time.Clock()

        # --- Criar a bola --- #
        self.bola = Bola(self.TELA)

        # --- Criar as raquetes --- #
        self.jogador_1 = Raquete(self.TELA, 'jogador_1')
        self.jogador_2 = Raquete(self.TELA, 'jogador_2')

        # --- Criar o HUD --- #
        self.hud = HUD(self.TELA)

    def executar(self) -> None:
        """Função responsável por executar o jogo."""
        # --- Game loop: coração do jogo --- #
        while True:
            # --- Lidar com eventos --- #
            for evento in pygame.event.get():
                # --- Se o evento for fechar a tela --- #
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # --- Obter o estado das teclas --- #
            teclas = pygame.key.get_pressed()

            # --- Raquete do jogador 1 --- #
            if teclas[pygame.K_w]:
                self.jogador_1.atualizar(True)
            if teclas[pygame.K_s]:
                self.jogador_1.atualizar(False)

            # --- Raquete do jogador 2 --- #
            if self.multiplayer:
                if teclas[pygame.K_UP]:
                    self.jogador_2.atualizar(True)
                if teclas[pygame.K_DOWN]:
                    self.jogador_2.atualizar(False)
            else:
                margem = 5
                if self.jogador_2.rect().centerx < self.bola.bola_x + LARGURA_TELA // 6:
                    if self.jogador_2.rect().centery < self.bola.bola_y + margem:
                        self.jogador_2.raquete_y += self.jogador_2.velocidade
                    elif self.jogador_2.rect().centery > self.bola.bola_y + margem:
                        self.jogador_2.raquete_y -= self.jogador_2.velocidade

            # --- Atualizar a posição da bola --- #
            self.bola.atualizar(self.jogador_1.rect(), self.jogador_2.rect())

            # --- Preencher a tela --- #
            self.TELA.fill(PRETO)

            # --- Desenhar a bola na tela --- #
            self.bola.renderizar()

            # --- Desenhar as raquetes na tela --- #
            self.jogador_1.renderizar()
            self.jogador_2.renderizar()

            # --- Colocar o placar do jogador 1 --- #
            self.hud.renderizar(
                self.bola.pontuacao_jogador_1,
                [LARGURA_TELA // 4, 50]
            )

            # --- Colocar o placar do jogador 2 --- #
            self.hud.renderizar(
                self.bola.pontuacao_jogador_2,
                [LARGURA_TELA * 3 // 4, 50]
            )

            # --- Fixar o FPS --- #
            self.clock.tick(60)

            # --- Atualizar a tela --- #
            pygame.display.flip()


if __name__ == '__main__':
    Pong(False).executar()
