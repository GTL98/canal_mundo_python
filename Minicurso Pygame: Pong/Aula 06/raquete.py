# --- Importar o Pygame --- #
import pygame

# --- Importar o módulo das configurações --- #
from configuracoes import *


class Raquete:
    """Classe responsável pela raquete."""
    def __init__(self, superficie, jogador):
        """Função que inicializa a classe."""
        # --- Tela do jogo --- #
        self.superficie = superficie

        # --- Configurações da raquete --- #
        self.altura = 100
        self.largura = 10
        self.velocidade = 6

        # --- Verificar qual jogador é para colocar a raquete no jogo --- #
        if jogador == 'jogador_1':
            self.raquete_x = 50
        if jogador == 'jogador_2':
            self.raquete_x = LARGURA_TELA - 50 - self.largura

        # --- Posição no eixo Y --- #
        self.raquete_y = ALTURA_TELA // 2 - self.altura // 2

    def rect(self) -> pygame.Rect:
        """Função responsável por criar o rect da raquete."""
        return pygame.Rect(
            self.raquete_x,
            self.raquete_y,
            self.largura,
            self.altura
        )

    def raquete(self) -> pygame.draw.rect:
        """Função responsável por desenhar a raquete."""
        return pygame.draw.rect(
            surface=self.superficie,
            color=BRANCO,
            rect=self.rect()
        )

    def colisao(self) -> None:
        """Função responsável por verificar a colisão com o topo e a base da tela."""
        # --- Obter o objeto rect da raquete --- #
        rect_raquete = self.rect()

        # --- Limitar o movimento da raquete na tela --- #
        if rect_raquete.top <= 0:
            rect_raquete.top = 0
        if rect_raquete.bottom >= ALTURA_TELA:
            rect_raquete.bottom = ALTURA_TELA

        # --- Atualizar a colisão --- #
        self.raquete_y = rect_raquete.y

    def atualizar(self, sobe: bool) -> None:
        """
        Função responsável por atualziar a raquete.
        :param sobe: Valor booleano para indicar se a raquete sobe ou não.
        """
        # --- Movimentar a raquete --- #
        if sobe:
            self.raquete_y -= self.velocidade
        else:
            self.raquete_y += self.velocidade

        # --- Verificar a colisão --- #
        self.colisao()

    def renderizar(self) -> None:
        """Função responsável por renderizar a raquete."""
        # --- Desenhar a raquete --- #
        self.raquete()
