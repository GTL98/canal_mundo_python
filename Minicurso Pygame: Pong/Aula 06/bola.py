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

        # --- Pontuação do jogadores --- #
        self.pontuacao_jogador_1 = 0
        self.pontuacao_jogador_2 = 0

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

    def colisao(self, rect_raquete_1: pygame.Rect, rect_raquete_2: pygame.Rect) -> None:
        """
        Função responsável por verificar a colisão da bola.
        :param rect_raquete_1: Objeto rect da raquete do jogador 1.
        :param rect_raquete_2: Objeto rect da raquete do jogador 2.
        """
        # --- Obter o rect da bola --- #
        bola_rect = self.rect()

        # --- Verificar a colisão da bola com o topo e a base da tela --- #
        if bola_rect.top <= 0 or bola_rect.bottom >= ALTURA_TELA:
            self.velocidade_y *= -1

        # --- Verificar se a bola colidiu com a raquete do jogador 1 --- #
        if bola_rect.colliderect(rect_raquete_1):
            self.velocidade_x *= -1
            self.bola_x = rect_raquete_1.right + self.raio
            bola_rect.center = (self.bola_x, self.bola_y)

        # --- Verificar se a bola colidiu com a raquete do jogador 2 --- #
        if bola_rect.colliderect(rect_raquete_2):
            self.velocidade_x *= -1
            self.bola_x = rect_raquete_2.left - self.raio
            bola_rect.center = (self.bola_x, self.bola_y)

        # --- Verificar se a bola colidiu com a parede direita da tela (ponto do jogador 1) --- #
        if bola_rect.right >= LARGURA_TELA:
            self.pontuacao_jogador_1 += 1
            self.bola_x = LARGURA_TELA // 2
            self.bola_y = ALTURA_TELA // 2
            bola_rect.center = (self.bola_x, self.bola_y)
            self.velocidade_x *= -1
            self.velocidade_y *= -1
            pygame.time.delay(500)

        # --- Verificar se a bola colidiu com a parede esquerda da tela (ponto do jogador 2) --- #
        if bola_rect.left <= 0:
            self.pontuacao_jogador_2 += 1
            self.bola_x = LARGURA_TELA // 2
            self.bola_y = ALTURA_TELA // 2
            bola_rect.center = (self.bola_x, self.bola_y)
            self.velocidade_x *= -1
            self.velocidade_y *= -1
            pygame.time.delay(500)

    def atualizar(self, rect_raquete_1: pygame.Rect, rect_raquete_2: pygame.Rect) -> None:
        """
        Função responsável por atualizar a bola.
        :param rect_raquete_1: Objeto rect da raquete do jogador 1.
        :param rect_raquete_2: Objeto rect da raquete do jogador 2.
        """
        # --- Movimentar a bola no eixo X --- #
        self.bola_x += self.velocidade_x

        # --- Movimentar a bola no eixo Y --- #
        self.bola_y += self.velocidade_y

        # --- Verificar a colisão da bola --- #
        self.colisao(rect_raquete_1, rect_raquete_2)

    def renderizar(self) -> None:
        """Função responsável por renderizar a bola."""
        # --- Desenhar a bola --- #
        self.bola()
