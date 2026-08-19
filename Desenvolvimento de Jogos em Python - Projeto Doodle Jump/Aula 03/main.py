# --- Importar os módulos --- #
import sys
import random
import pygame

# --- Importar as configurações --- #
from config import *

# --- Importar as classes --- #
from jogador import Jogador
from plataforma import Plataforma


class DoodleJump:
    def __init__(self):
        # --- Inicializar o Pygame --- #
        pygame.init()

        # --- Configurar a tela do jogo --- #
        self.TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption('Python Doodle Jump')

        # --- Controlador de FPS --- #
        self.relogio = pygame.time.Clock()

        # --- Flag de execução do jogo --- #
        self.rodando = True

        # --- Instanciar o jogador --- #
        self.jogador = Jogador()

        # --- Lista de plataformas --- #
        self.plataformas = []
        self.gerar_plataformas_iniciais()

    def gerar_plataformas_iniciais(self):
        # --- Criar o chão e as plataformas em degraus --- #
        chao = Plataforma(0, ALTURA_TELA - 20, LARGURA_TELA, 20)
        plat_1 = Plataforma(LARGURA_TELA // 2 - 50, ALTURA_TELA - 150, 100, 20)
        plat_2 = Plataforma(LARGURA_TELA // 4 - 50, ALTURA_TELA - 250, 100, 20)
        plat_3 = Plataforma(LARGURA_TELA // 1.5 - 50, ALTURA_TELA - 350, 100, 20)

        # --- Adicionar tudo à lista --- #
        self.plataformas.extend([chao, plat_1, plat_2, plat_3])

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
        # --- Movimentar o jogador --- #
        self.jogador.mover()

        # --- Lógica de colisão com o chão --- #
        # --- Só quica se o jogador estiver caindo (velocidade_y > 0) --- #
        if self.jogador.velocidade_y > 0:
            for plat in self.plataformas:
                if self.jogador.rect.colliderect(plat.rect):
                    # --- Checagem extra: garante que ele só quica se bater com o pé no topo da plataforma --- #
                    if self.jogador.rect.bottom <= plat.rect.top + 20:
                        self.jogador.velocidade_y = FORCA_PULO
                        break  # se colidiu com uma plataforma, não precisa verificar com outras

        # --- Lógica da câmera --- #
        if self.jogador.rect.top <= LINHA_SCROLL and self.jogador.velocidade_y < 0:
            # --- Obter a velocidade --- #
            scroll = abs(self.jogador.velocidade_y)

            # --- Travar o jogador na linha --- #
            self.jogador.rect.top = LINHA_SCROLL

            # --- Empurrar todas as plataformas para baixo --- #
            for plat in self.plataformas:
                plat.rect.y += scroll

        # --- Geração procedural --- #
        # --- Limpar as plataformas que saírem da tela por baixo --- #
        for plat in self.plataformas[:]:
            if plat.rect.top >= ALTURA_TELA:
                self.plataformas.remove(plat)

        # --- Gerar novas plataformas no topo --- #
        while len(self.plataformas) < 6:
            # --- Sortear uma largura para a nova plataforma --- #
            largura = random.randint(50, 100)

            # --- Posição X aleatória --- #
            x = random.randint(0, LARGURA_TELA - largura)

            # --- Descobrir qual é a plataforma mais alta --- #
            y_mais_alto = min([plat.rect.y for plat in self.plataformas])

            # --- Posição Y da nova plataforma será um pouco acima da mais alta --- #
            y = y_mais_alto - random.randint(80, 120)

            # --- Adicionar as plataformas à lista --- #
            nova_plataforma = Plataforma(x, y, largura, 20)
            self.plataformas.append(nova_plataforma)

    def desenhar(self):
        # --- Desenhar na tela --- #
        self.TELA.fill(BRANCO)

        # --- Desenhar os objetos do jogo --- #
        for plat in self.plataformas:
            plat.desenhar(self.TELA)
        self.jogador.desenhar(self.TELA)

        # --- Atualizar a tela --- #
        pygame.display.flip()

    def rodar(self):
        # --- Exutar o jogo --- #
        while self.rodando:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()
            self.relogio.tick(FPS)

        # --- Fechar a tela quando fechar o jogo --- #
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    jogo = DoodleJump()
    jogo.rodar()