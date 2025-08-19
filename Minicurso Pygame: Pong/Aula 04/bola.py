# --- Importar o Pygame --- #
import pygame

# --- Importar o módulo das configurações --- #
from configuracoes import *


class Bola:
    """Classe responsável pela bola."""
    def __init__(self, superficie):
        """Função responsável por inicializar a classe."""
        # --- Tela do jogo --- #
        self.superficie = superficie

        # --- Configurações da bola --- #
        self.raio = 10
        self.velocidade_x = 5
        self.velocidade_y = 5

        # --- Posição inicial da bola --- #
        self.bola_x = LARGURA_TELA // 2
        self.bola_y = ALTURA_TELA // 2

    def rect(self) -> pygame.Rect:
        """Função responsável por criar o rect da bola."""
        # --- Altura e largura da bola --- #
        altura = self.raio * 2
        largura = self.raio * 2

        return pygame.Rect(
            self.bola_x - self.raio,
            self.bola_y - self.raio,
            largura,
            altura
        )

    def bola(self) -> pygame.draw.circle:
        """Função responsável por desenhar a bola."""
        return pygame.draw.circle(
            surface=self.superficie,
            color=BRANCO,
            center=(self.bola_x, self.bola_y),
            radius=self.raio
        )

    def colisao(self) -> None:
        """Função responsável por verificar a colisão da bola."""
        # --- Obter o rect da bola --- #
        bola_rect = self.rect()

        # --- Verificar a colisão da bola com o topo e a base da tela --- #
        if bola_rect.top <= 0 or bola_rect.bottom >= ALTURA_TELA:
            self.velocidade_y *= -1

    def atualizar(self) -> None:
        """Função responsável por atualizar a bola."""
        # --- Movimentar a bola no eixo X --- #
        self.bola_x += self.velocidade_x

        # --- Movimentar a bola no eixo Y --- #
        self.bola_y += self.velocidade_y

        # --- Verificar a colisão da bola --- #
        self.colisao()

    def renderizar(self) -> None:
        """Função responsável por renderizar a bola."""
        # --- Desenhar a bola --- #
        self.bola()
