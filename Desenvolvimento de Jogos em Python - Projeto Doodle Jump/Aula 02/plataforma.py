# --- Importar o Pygame --- #
import pygame

# --- Importar as configurações --- #
from config import *


class Plataforma:
    def __init__(self, x, y, largura, altura):
        # --- Criar o objeto Rect da plataforma --- #
        self.rect = pygame.Rect(x, y, largura, altura)

    def desenhar(self, tela):
        # --- Desenhar a plataforma na tela --- #
        pygame.draw.rect(tela, VERDE, self.rect)