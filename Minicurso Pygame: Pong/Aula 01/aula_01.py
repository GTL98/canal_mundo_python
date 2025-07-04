# --- Importar as bibliotecas --- #
import sys
import pygame

# --- Inicializar o Pygame --- #
pygame.init()

# --- Configurações da tela --- #
ALTURA_TELA = 600
LARGURA_TELA = 800

# --- Criar a tela --- #
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# --- Definir o título da tela --- #
pygame.display.set_caption('Pong')

# --- Cores do jogo --- #
PRETO = (0, 0, 0)

# --- Game loop: o coração do jogo --- #
while True:
    # --- Lidar com eventos --- #
    for evento in pygame.event.get():
        # --- Se o evento for fechar a tela --- #
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Preencher a tela --- #
    TELA.fill(PRETO)

    # --- Atualizar a tela --- #
    pygame.display.flip()
