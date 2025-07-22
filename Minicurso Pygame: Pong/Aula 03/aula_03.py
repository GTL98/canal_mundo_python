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

# --- Configurações das raquetes --- #
ALTURA_RAQUETE = 100
LARGURA_RAQUETE = 10
VELOCIDADE_RAQUETE = 0.5

# --- Raquete do jogador 1 (esquerda) --- #
raquete_1_x = 50
raquete_1_y = ALTURA_TELA // 2 - ALTURA_RAQUETE // 2
raquete_1_rect = pygame.Rect(
    raquete_1_x,
    raquete_1_y,
    LARGURA_RAQUETE,
    ALTURA_RAQUETE
)

# --- Raquete do jogador 2 (direita) --- #
raquete_2_x = LARGURA_TELA - 50 - LARGURA_RAQUETE
raquete_2_y = ALTURA_TELA // 2 - ALTURA_RAQUETE // 2
raquete_2_rect = pygame.Rect(
    raquete_2_x,
    raquete_2_y,
    LARGURA_RAQUETE,
    ALTURA_RAQUETE
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
    if bola_rect.top <= 0 or bola_rect.bottom >= ALTURA_TELA:
        VELOCIDADE_BOLA_Y *= -1

    # --- Obter o estado das teclas --- #
    teclas = pygame.key.get_pressed()

    # --- Raquete do jogador 1 (esquerda) --- #
    if teclas[pygame.K_w]:
        raquete_1_y -= VELOCIDADE_RAQUETE
    if teclas[pygame.K_s]:
        raquete_1_y += VELOCIDADE_RAQUETE

    # --- Raquete do jogador 2 (direita) --- #
    if teclas[pygame.K_UP]:
        raquete_2_y -= VELOCIDADE_RAQUETE
    if teclas[pygame.K_DOWN]:
        raquete_2_y += VELOCIDADE_RAQUETE

    # --- Atualizar a posição dos rects das raquetes --- #
    raquete_1_rect.y = raquete_1_y
    raquete_2_rect.y = raquete_2_y

    # --- Limitar o movimento da raquete 1 na tela --- #
    if raquete_1_rect.top <= 0:
        raquete_1_rect.top = 0
    if raquete_1_rect.bottom >= ALTURA_TELA:
        raquete_1_rect.bottom = ALTURA_TELA

    # --- Limitar o movimento da raquete 2 na tela --- #
    if raquete_2_rect.top <= 0:
        raquete_2_rect.top = 0
    if raquete_2_rect.bottom >= ALTURA_TELA:
        raquete_2_rect.bottom = ALTURA_TELA

    # --- Preencher a tela --- #
    TELA.fill(PRETO)

    # --- Desenhar a bola na tela --- #
    pygame.draw.circle(
        surface=TELA,
        color=BRANCO,
        center=(bola_x, bola_y),
        radius=RAIO_BOLA
    )

    # --- Desenhar as raquetes --- #
    pygame.draw.rect(
        surface=TELA,
        color=BRANCO,
        rect=raquete_1_rect
    )
    pygame.draw.rect(
        surface=TELA,
        color=BRANCO,
        rect=raquete_2_rect
    )

    # --- Atualizar a tela --- #
    pygame.display.flip()
