# --- Importar o Pygame --- #
import pygame

# --- Importar as configurações --- #
from config import *


class Jogador:
    def __init__(self):
        # --- Criar o objeto Rect do jogador --- #
        self.rect = pygame.Rect(
            LARGURA_TELA // 2 - LARGURA_JOGADOR // 2,
            ALTURA_TELA - 100,
            LARGURA_JOGADOR,
            ALTURA_JOGADOR
        )
        self.velocidade_x = 0
        self.velocidade_y = 0

        # --- Carregar a imagem do jogador --- #
        self.imagem_direita = pygame.image.load('./assets/sprites/jogador_direita.png').convert_alpha()
        self.imagem_direita = pygame.transform.scale(self.imagem_direita, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem_esquerda = pygame.image.load('./assets/sprites/jogador_esquerda.png').convert_alpha()
        self.imagem_esquerda = pygame.transform.scale(self.imagem_esquerda, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem = self.imagem_direita

    def mover(self):
        # --- Lista com as teclas do teclado --- #
        teclas = pygame.key.get_pressed()
        self.velocidade_x = 0

        # --- Verificar se foi pressionada alguma tecla e mover o jogador --- #
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.velocidade_x = -5
            self.imagem = self.imagem_esquerda

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.velocidade_x = 5
            self.imagem = self.imagem_direita

        # --- Atualizar o Rect do jogador --- #
        self.rect.x += self.velocidade_x

        # --- Verificar a colisão com as bordas (direita e esquerda) --- #
        if self.rect.right < 0:
            self.rect.left = LARGURA_TELA
        elif self.rect.left > LARGURA_TELA:
            self.rect.right = 0

        # --- Aplicar a gravidade --- #
        self.velocidade_y += GRAVIDADE
        self.rect.y += self.velocidade_y

    def desenhar(self, tela):
        # --- Desenhar o jogador na tela --- #
        tela.blit(self.imagem, self.rect)