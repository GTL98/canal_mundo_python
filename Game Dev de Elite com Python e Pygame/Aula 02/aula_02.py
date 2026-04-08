# --- Importar as bibliotecas --- #
import sys
import pygame
from pygame.math import Vector2


def main():
    # --- Inicialização do Pygame --- #
    pygame.init()

    # --- Configurações da janela principal --- #
    LARGURA, ALTURA = 1280, 720
    TELA = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Aula 02: Desenho geométrico e API de cores')

    # --- Controlador de FPS --- #
    CLOCK = pygame.time.Clock()

    # --- Usar os novos métodos para cores --- #
    COR_FUNDO = pygame.Color('#1a1a2e')  # azul escuro profundo

    # --- A API permite criar cores a partir de HEX de forma direta no construtor --- #
    COR_PRIMARIA = pygame.Color.from_hex('#e94560')  # rosa vibrante
    COR_SECUNDARIA = pygame.Color.from_hex('#0f3460')  # azul marinho intermediário

    # --- Cores por nome suportadas nativamente pelo Pygame --- #
    COR_BORDA = pygame.Color('ghostwhite')

    # --- Criar uma surfaxe para evitar que o flood_fill seja apagado a cada frame --- #
    canvas = pygame.Surface((LARGURA, ALTURA))
    canvas.fill(COR_FUNDO)

    # --- Game loop --- #
    rodando = True
    while rodando:
        # --- Gestão de eventos --- #
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # --- Interatividade com o flood_fill --- #
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # botão esquerdo
                    # --- Aplicar a "lata de tinta" no canvas --- #
                    pygame.draw.flood_fill(canvas, COR_PRIMARIA, evento.pos)

        # --- Adicionar o canvas na tela --- #
        TELA.blit(canvas, (0, 0))

        # --- Desenhar um retângulo sólido --- #
        # --- Criamos um objeto Rect (x, y, largura, altura) --- #
        caixa_menu = pygame.Rect(100, 100, 300, 200)
        pygame.draw.rect(TELA, COR_PRIMARIA, caixa_menu, border_radius=20)

        # --- Retângulo apenas com contorno --- #
        pygame.draw.rect(TELA, COR_BORDA, caixa_menu, width=4, border_radius=20)

        # --- Retângulo com cantos arredondados assimétricos --- #
        aba_inventario = pygame.Rect(100, 350, 300, 100)
        pygame.draw.rect(TELA, COR_SECUNDARIA, aba_inventario,
                         border_top_left_radius=40,
                         border_bottom_right_radius=40)

        # --- Círculo centralizado usando Vector2 para precisão --- #
        # --- O uso de float evitar o "jitter" durante o movimento --- #
        pos_centro = Vector2(800, 200)
        pygame.draw.circle(TELA, COR_PRIMARIA, pos_centro, 80)

        # --- Efeito de "carga" usando quadrantes --- #
        # --- Ideal para medidores de vida ou timers radiais --- #
        pygame.draw.circle(TELA, COR_BORDA, (800, 450), 60, width=8,
                           draw_top_left=True, draw_top_right=True, draw_bottom_left=True)

        # --- São excelentes para sombras sob personagens ou efeitos de perspectiva --- #
        guia_elipse = pygame.Rect(650, 550, 300, 100)
        pygame.draw.ellipse(TELA, COR_SECUNDARIA, guia_elipse)
        pygame.draw.ellipse(TELA, COR_BORDA, guia_elipse, width=2)

        # --- Desenhar um polígono --- #
        pontos_triangulo = [(1100, 100), (1000, 300), (1200, 300)]
        pygame.draw.polygon(TELA, 'orange', pontos_triangulo)
        pygame.draw.polygon(TELA, COR_BORDA, pontos_triangulo, width=3)

        # --- Linha única com espessura --- #
        pygame.draw.line(TELA, 'cyan', (50, 680), (1230, 680), width=10)

        # --- Linhas conectadas --- #
        caminho_irregular = [(500, 50), (550, 100), (600, 20), (650, 100)]
        pygame.draw.lines(TELA, 'magenta', False, caminho_irregular, width=5)

        # --- Atualizar a tela --- #
        pygame.display.flip()

        # --- Limitar o FPS --- #
        CLOCK.tick(60)

    # --- Encerramento limpo do motor e o sistema operacional --- #
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()