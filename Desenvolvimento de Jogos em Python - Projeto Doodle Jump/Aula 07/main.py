# --- Importar os módulos --- #
import os
import sys
import random
import pygame

# --- Importar as configurações --- #
from config import *

# --- Importar as classes --- #
from jogador import Jogador
from inimigo import Inimigo
from plataforma import Plataforma

# --- Importar o módulo do caminho --- #
from caminho_assets import caminho_assets

# --- Importar o módulo de salvamento do highscore --- #
from salvar_arquivo_highscore import salvar_arquivo_highscore


class DoodleJump:
    def __init__(self):
        # --- Inicializar o Pygame --- #
        pygame.init()

        # --- Inicializar o mixer de áudio --- #
        pygame.mixer.init()

        # --- Carregar os áudios --- #
        self.som_iniciar = pygame.mixer.Sound(caminho_assets('assets/audio/iniciar.wav'))
        self.som_pulo = pygame.mixer.Sound(caminho_assets('assets/audio/pulo.wav'))
        self.som_game_over_queda = pygame.mixer.Sound(caminho_assets('assets/audio/game_over_queda.mp3'))
        self.som_game_over_inimigo = pygame.mixer.Sound(caminho_assets('assets/audio/game_over_inimigo.mp3'))

        # --- Configurar a tela do jogo --- #
        self.TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption('Python Doodle Jump')

        # --- Adicionar o ícone à tela do jogo --- #
        caminho_icone = caminho_assets('assets/sprites/icone/icone.ico')
        icone = pygame.image.load(caminho_icone).convert_alpha()
        pygame.display.set_icon(icone)

        # --- Controlador de FPS --- #
        self.relogio = pygame.time.Clock()

        # --- Flag de execução do jogo --- #
        self.rodando = True

        # --- Variáveis de placar e fonte --- #
        self.fonte = pygame.font.SysFont('Arial', 24, True)
        self.fonte_game_over = pygame.font.SysFont('Arial', 40, True)
        self.fonte_titulo = pygame.font.SysFont('Arial', 60, True)

        # --- Carregar o highscore ao abrir o jogo --- #
        self.highscore = 0
        self.carregar_highscore()

        # --- Estados iniciais do jogo --- #
        self.tela_inicial = True
        self.resetar_jogo()

        # --- Carregar a imagem do fundo --- #
        caminho_imagem = caminho_assets('assets/sprites/fundo/fundo.png')
        self.imagem_fundo = pygame.image.load(caminho_imagem).convert_alpha()
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (LARGURA_TELA, ALTURA_TELA))
        self.fundo_y = 0  # controle da posiçãpo Y no fundo

    def carregar_highscore(self):
        # --- Usar a função para descobrir onde está o arquivo --- #
        caminho_arquivo = salvar_arquivo_highscore('highscore.txt')

        # --- Tentar ler o arquivo TXT. Se não existir, o recorde é 0 --- #
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'r') as txt:
                try:
                    self.highscore = float(txt.read())
                except ValueError:
                    self.highscore = 0

    def salvar_highscore(self):
        # --- Usar a função para descobrir onde está o arquivo e salvar --- #
        caminho_arquivo = salvar_arquivo_highscore('highscore.txt')

        # --- Criar ou substituir o arquivo TXT com o novo recorde --- #
        with open(caminho_arquivo, 'w') as txt:
            txt.write(str(self.highscore))

    def resetar_jogo(self):
        # --- Função para começar ou recomeçar a partida --- #
        self.som_iniciar.play()
        self.game_over = False
        self.pontuacao = 0
        self.jogador = Jogador()
        self.plataformas = []
        self.inimigos = []
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

            # --- Detectar se apertou espaço para reiniciar --- #
            if evento.type == pygame.KEYDOWN:
                if self.tela_inicial:
                    self.tela_inicial = False  # sai da tela inicial se qualquer tecla for apertada
                if evento.key == pygame.K_SPACE and self.game_over:
                    self.resetar_jogo()

    def atualizar(self):
        # --- O jogo só atualiza se não estiver em game over --- #
        if not self.game_over and not self.tela_inicial:
            # --- Movimentar o jogador --- #
            self.jogador.mover()

            # --- Atualizar inimigos e colisão --- #
            for inimigo in self.inimigos:
                inimigo.atualizar()

                # --- Contato do jogador com o inimigo --- #
                if self.jogador.rect.colliderect(inimigo.rect):
                    self.som_game_over_inimigo.play()
                    self.game_over = True

                    # --- Verificar se quebrou o recorde e salvar --- #
                    if self.pontuacao > self.highscore:
                        self.highscore = self.pontuacao
                        self.salvar_highscore()

            # --- Lógica de colisão com o chão --- #
            # --- Só quica se o jogador estiver caindo (velocidade_y > 0) --- #
            if self.jogador.velocidade_y > 0:
                for plat in self.plataformas:
                    if self.jogador.rect.colliderect(plat.rect):
                        # --- Checagem extra: garante que ele só quica se bater com o pé no topo da plataforma --- #
                        if self.jogador.rect.bottom <= plat.rect.top + 20:
                            self.jogador.velocidade_y = FORCA_PULO
                            self.som_pulo.play()
                            break  # se colidiu com uma plataforma, não precisa verificar com outras

            # --- Lógica da câmera --- #
            if self.jogador.rect.top <= LINHA_SCROLL and self.jogador.velocidade_y < 0:
                # --- Obter a velocidade --- #
                scroll = abs(self.jogador.velocidade_y)

                # --- Travar o jogador na linha --- #
                self.jogador.rect.top = LINHA_SCROLL

                # --- Incrementar a pontuação --- #
                self.pontuacao += scroll

                # --- Empurrar todas as plataformas para baixo --- #
                for plat in self.plataformas:
                    plat.rect.y += scroll

                # --- Empurrar os inimigos para baixo --- #
                for inimigo in self.inimigos:
                    inimigo.rect.y += scroll

                # --- Movimentar o fundo infinito --- #
                self.fundo_y += scroll
                if self.fundo_y >= ALTURA_TELA:
                    self.fundo_y = 0  # resetar a posição par criar o loop infinito

            # --- Geração procedural --- #
            # --- Limpar as plataformas que saírem da tela por baixo --- #
            for plat in self.plataformas[:]:
                if plat.rect.top >= ALTURA_TELA:
                    self.plataformas.remove(plat)

            # --- Limpar os inimigos que saírem da tela por baixo --- #
            for inimigo in self.inimigos[:]:
                if inimigo.rect.top >= ALTURA_TELA:
                    self.inimigos.remove(inimigo)

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

                # --- Gerar os inimigos --- #
                if random.randint(1, 100) <= 15:  # 15% de chance
                    novo_inimigo = Inimigo(
                        x,
                        y - ALTURA_INIMIGO,
                        x - largura,
                        x + (largura * 2)
                    )
                    self.inimigos.append(novo_inimigo)

            # --- Condição de game over --- #
            if self.jogador.rect.top > ALTURA_TELA:
                self.som_game_over_queda.play()
                self.game_over = True

                # --- Verificar se quebrou o recorde e salvar --- #
                if self.pontuacao > self.highscore:
                    self.highscore = self.pontuacao
                    self.salvar_highscore()

    def desenhar(self):
        # --- Desenhar o fundo --- #
        self.TELA.blit(self.imagem_fundo, (0, self.fundo_y))
        self.TELA.blit(self.imagem_fundo, (0, self.fundo_y - ALTURA_TELA))

        # --- Estados visuais --- #
        if self.tela_inicial:
            # --- Desenhar a tela inicial --- #
            texto_titulo = self.fonte_titulo.render('DOODLE JUMP', True, AZUL)
            texto_instrucao = self.fonte.render('Pressione QUALQUER TECLA para iniciar', True, PRETO)

            self.TELA.blit(texto_titulo, (LARGURA_TELA // 2 - texto_titulo.get_width() // 2,
                                          ALTURA_TELA // 2 - 60))
            self.TELA.blit(texto_instrucao, (LARGURA_TELA // 2 - texto_instrucao.get_width() // 2,
                                             ALTURA_TELA // 2 + 20))
        else:
            # --- Desenhar os objetos do jogo --- #
            for plat in self.plataformas:
                plat.desenhar(self.TELA)

            for inimigo in self.inimigos:
                inimigo.desenhar(self.TELA)

            self.jogador.desenhar(self.TELA)

            # --- Renderizar e desenhar a pontuação --- #
            texto_placar = self.fonte.render(f'Pontuação: {int(self.pontuacao)}', True, PRETO)
            self.TELA.blit(texto_placar, (10, 10))

            # --- Renderizar e desenhar o recorde --- #
            texto_highscore = self.fonte.render(f'Recorde: {int(self.highscore)}', True, PRETO)
            self.TELA.blit(texto_highscore, (LARGURA_TELA // 2 - texto_highscore.get_width() // 2, 10))

            # --- Desenhar a tela de game over --- #
            if self.game_over:
                texto_game_over = self.fonte_game_over.render('GAME OVER', True, VERMELHO)
                texto_restart = self.fonte.render('Pressione ESPAÇO para reiniciar', True, PRETO)

                # --- Centralizar os textos --- #
                self.TELA.blit(texto_game_over, (LARGURA_TELA // 2 - texto_game_over.get_width() // 2,
                                                 ALTURA_TELA // 2 - 50))
                self.TELA.blit(texto_restart, (LARGURA_TELA // 2 - texto_restart.get_width() // 2,
                                               ALTURA_TELA // 2 + 20))

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