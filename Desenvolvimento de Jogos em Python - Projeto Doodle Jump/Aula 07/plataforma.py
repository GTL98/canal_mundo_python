# --- Importar os módulos--- #
import pygame
import random

# --- Importar as configurações --- #
from config import *

# --- Importar o módulo do caminho --- #
from caminho_assets import caminho_assets


class Plataforma:
    def __init__(self, x, y, largura, altura):
        # --- Criar o objeto Rect da plataforma --- #
        self.rect = pygame.Rect(x, y, largura, altura)

        # --- Sortear e carregar uma imagem aleatória --- #
        num_sprite = random.randint(1, 3)
        caminho_imagem = caminho_assets(f'assets/sprites/plataformas/plataforma_0{num_sprite}.png')

        # --- Carregar a redimensionar a imagem --- #
        self.imagem = pygame.image.load(caminho_imagem).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))

    def desenhar(self, tela):
        # --- Desenhar a plataforma na tela --- #
        tela.blit(self.imagem, self.rect)