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
BRANCO = (255, 255, 255)

# --- Configurações da bola --- #
RAIO_BOLA = 10  # raio visual da bola
VELOCIDADE_BOLA_X = 0.1  # velocidade horizontal da bola
VELOCIDADE_BOLA_Y = 0.1  # velocidade vertical da bola

# --- Posição inicial da bola (centro da tela) --- #
bola_x = LARGURA_TELA // 2
bola_y = ALTURA_TELA // 2

# --- Criar o objeto rect para a bola nas posições e dimensões (esquerda, topo, largura, altura) --- #
bola_rect = pygame.Rect(
    bola_x - RAIO_BOLA,
    bola_y - RAIO_BOLA,
    RAIO_BOLA * 2,
    RAIO_BOLA * 2
)

# --- Game loop: o coração do jogo --- #
while True:
    # --- Lidar com eventos --- #
    for evento in pygame.event.get():
        # --- Se o evento for fechar a tela --- #
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Movimento da bola --- #
    bola_x += VELOCIDADE_BOLA_X
    bola_y += VELOCIDADE_BOLA_Y

    # --- Atualizar a posição do rect da bola para corresponder ao movimento --- #
    bola_rect.center = (bola_x, bola_y)

    # --- Se a bola tocar na borda superior OU inferior --- #
    if bola_y - RAIO_BOLA <= 0 or bola_y + RAIO_BOLA >= ALTURA_TELA:
        VELOCIDADE_BOLA_Y *= -1

    # --- Preencher a tela --- #
    TELA.fill(PRETO)

    # --- Desenhar a bola na tela --- #
    pygame.draw.circle(
        surface=TELA,
        color=BRANCO,
        center=(bola_x, bola_y),
        radius=RAIO_BOLA
    )

    # --- Atualizar a tela --- #
    pygame.display.flip()
