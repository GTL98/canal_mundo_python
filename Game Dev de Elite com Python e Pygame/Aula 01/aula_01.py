# --- Importar as bibliotecas --- #
import sys
import pygame

# --- Inicialização global de todos os módulos carregados do Pygame --- #
pygame.init()

# --- Configurações das dimensões da janela --- #
ALTURA = 720
LARGURA = 1280
TELA = pygame.display.set_mode((LARGURA, ALTURA))

# --- Definição do título que aparecerá no topo da tela --- #
pygame.display.set_caption('Aula 01')

# --- Controle da cadência temporal e limite de FPS --- #
CLOCK = pygame.time.Clock()

# --- Variável para manter o motor em funcionamento --- #
rodando = True

# --- Início do Game loop --- #
while rodando:
    # --- O código interno aqui será rodado repetidamente --- #
    # --- Gerenciamento de eventos --- #
    for evento in pygame.event.get():
        # --- Verificar se o evento é o fechamento da janela --- #
        if evento.type == pygame.QUIT:
            rodando = False

    # --- Preenchimento do fundo da janela --- #
    TELA.fill('midnightblue')

    # --- Atualizar a tela --- #
    pygame.display.flip()

    # --- Limitar o FPS do jogo --- #
    CLOCK.tick(60)

# --- Desativar os módulos do Pygame --- #
pygame.quit()  # contrário do pygame.init()

# --- Finalizar o processo do interpretador Python --- #
sys.exit()