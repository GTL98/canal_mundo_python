# --- Importar os módulos --- #
import pygame
import random

# --- Importar as configurações --- #
from config import *


class Inimigo:
    def __init__(self, x, y, limite_esq, limite_dir):
        # --- Criar o objeto Rect --- #
        self.rect = pygame.Rect(x, y, LARGURA_INIMIGO, ALTURA_INIMIGO)

        # --- Limites da patrulha --- #
        self.limite_esq = limite_esq
        self.limite_dir = limite_dir

        # --- Velocidade inicial aleatória --- #
        self.velocidade = 3 if random.choice([True, False]) else -3

        # --- Sorteio da imagem do inimigo --- #
        num_sprite = random.randint(1, 5)
        caminho = f'./assets/sprites/inimigos/inimigo_0{num_sprite}.png'

        # --- Carregar e redimensionar a imagem --- #
        self.imagem = pygame.image.load(caminho).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (LARGURA_INIMIGO, ALTURA_INIMIGO))

    def atualizar(self):
        # --- Mover o inimigo --- #
        self.rect.x += self.velocidade

        # --- Bater no limite da plataforma e voltar --- #
        if self.rect.left <= self.limite_esq or self.rect.right >= self.limite_dir:
            self.velocidade *= -1

    def desenhar(self, tela):
        # --- Desenhar o inimigo na tela --- #
        tela.blit(self.imagem, self.rect)