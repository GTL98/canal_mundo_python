# --- Importar o Pygame --- #
import pygame

# --- Importar as configurações --- #
from configuracoes import BRANCO


class HUD:
    """Classe responsável pela HUD do jogo."""
    def __init__(self, superficie):
        """Função responsável por inicializar a classe."""
        self.superficie = superficie
        self.fonte = pygame.font.Font(None, 74)

    def renderizar(self, pontos, posicao) -> None:
        """
        Função responsável por renderizar a pontuação.
        :param pontos: Pontos do jogador.
        :param posicao: Posição do texto na tela.
        """
        # --- Criar o objeto de renderização --- #
        pontos_obj = self.fonte.render(
            text=str(pontos),
            antialias=True,
            color=BRANCO
        )

        # --- Criar o objeto rect do texto --- #
        pontos_rect = pontos_obj.get_rect()

        # --- Ajustar a posição do placar --- #
        pontos_rect.center = posicao

        # --- Colocar na tela o placar --- #
        self.superficie.blit(pontos_obj, pontos_rect)
