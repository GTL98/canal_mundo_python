# --- Importar as bibliotecas --- #
import cv2
import mediapipe as mp


class DetectorMalhaRosto:
    """Classe responsável por detectar a malha do rosto."""
    def __init__(self, modo=False, max_rostos=2, refinar_pontos=False, deteccao_confianca=0.5,
                 rastreio_confianca=0.5, cor_pontos=(255, 255, 255), cor_conexoes=(0, 255, 0)):
        """
        Função responsável por inicializar a classe.
        :param modo: Modo de captura da imagem. Se True, a detecção e o rastrio serão feitos a todo momento;
        deixa muito travado. Se False, não são feitas a detecção e rastrio a todo momento; pode poerder
        pos alguns instântes as marcações, porém não trava.
        :param max_rostos: Quantidade máxima de rostos para serem detectados.
        :param refinar_pontos: Refinar as coordenadas dos pontos da baco e dos olhos.
        :param deteccao_confianca: Percentual da taxa de detecção do rosto. Se for menor do que este limite,
        a detecção não ocorre.
        :param rastreio_confianca:  Percentual da taxa do rastreio do rosto. Se for menor do que este limite,
        o rastreio não ocorre.
        :param cor_pontos: Cor dos pontos.
        :param cor_conexoes: Cor das conexões.
        """
        # --- Inicializar os parâmetros --- #
        self.modo = modo
        self.max_rostos = max_rostos
        self.refinar_pontos = refinar_pontos
        self.deteccao_confianca = deteccao_confianca
        self.rastreio_confianca = rastreio_confianca
        self.cor_pontos = cor_pontos
        self.cor_conexoes = cor_conexoes

        # --- Inicializar a função de detecção da malha do rosto --- #
        self.malha_rosto_mp = mp.solutions.face_mesh
        self.malha_rosto = self.malha_rosto_mp.FaceMesh(
            self.modo,
            self.max_rostos,
            self.refinar_pontos,
            self.deteccao_confianca,
            self.rastreio_confianca
        )
        self.malha_rosto_conexoes = mp.solutions.face_mesh_connections

        # --- Função para desenhar a malha no rosto --- #
        self.desenho_mp = mp.solutions.drawing_utils

        # --- Configurações do desenho dos pontos --- #
        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(
            color=self.cor_pontos,  # cor dos pontos
            thickness=1,  # espessura do pontos
            circle_radius=1,  # raio do ponto
        )

        # --- Configurações do desenho das conexões --- #
        self.desenho_config_conexoes = self.desenho_mp.DrawingSpec(
            color=self.cor_conexoes,
            thickness=1
        )

    def encontrar_malha_rosto(self, imagem, desenho=True):
        """
        Função responsável por detectar o(s) rosto(s).
        :param imagem: Imagem capturada.
        :param desenho: Desenhar a malha no(s) rosto(s).
        :return: Retorna a imagem com a malha facial.
        """
        # --- Conveter a imagem de BGR para RGB --- #
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

        # --- Passar a imagem convertida para o detector --- #
        self.resultado = self.malha_rosto.process(imagem_rgb)

        # --- Verificar se ocorreu a detecção do rosto --- #
        if self.resultado.multi_face_landmarks:
            # --- Obter os pontos da malha facial --- #
            for ponto_rosto in self.resultado.multi_face_landmarks:
                if desenho:
                    # --- Desenhar os pontos da malha --- #
                    self.desenho_mp.draw_landmarks(
                        imagem,  # imagem a ser desenhada
                        ponto_rosto,  # pontos da malha
                        self.malha_rosto_conexoes.FACEMESH_CONTOURS,  # conxões entre os pontos da malha
                        self.desenho_config_pontos,  # configuração do desenho dos pontos
                        self.desenho_config_conexoes  # configuração do desenho das conexões
                    )

        return imagem

    def encontrar_pontos(self, imagem):
        """
        Função responsável por informar os pontos da malha facial.
        :param imagem: Imagem capturada.
        :return: Retorna a lista com os pontos da malha do(s) rosto(s) detectado(s).
        """
        # --- Lista com os pontos dos rostos --- #
        rostos = []

        # --- Verificar se ocorreu a detecção do rosto --- #
        if self.resultado.multi_face_landmarks:
            # --- Obter os pontos da malha facial --- #
            for pontos_rosto in self.resultado.multi_face_landmarks:
                # --- Lista com a malha do rosto detectado --- #
                rosto = []

                # --- Obter a informação de cada ponto da malha --- #
                for id, ponto in enumerate(pontos_rosto.landmark):
                    # --- Conveter os valores de posição em pixels --- #
                    altura, largura, _ = imagem.shape
                    x, y = int(ponto.x * largura), int(ponto.y * altura)

                    # --- Adicionar à lista de rosto os pontos do rosto --- #
                    rosto.append([id, x, y])

                # --- Adicionar a lista com os pontos do rosto à lista de rostos detectados --- #
                rostos.append(rosto)

        return rostos


def main():
    # --- Captura da webcam --- #
    cap = cv2.VideoCapture(0)

    # --- Instanciar o detector da malha facial --- #
    detector = DetectorMalhaRosto()

    # --- Loop de captura --- #
    while True:
        # --- Captura da imagem --- #
        _, imagem = cap.read()

        # --- Inverter a imagem --- #
        imagem = cv2.flip(imagem, 1)

        # --- Detectar a malha do rosto --- #
        imagem = detector.encontrar_malha_rosto(imagem)

        # --- Mostrar a captura --- #
        cv2.imshow('Captura', imagem)

        # --- Tempo de atualização da captura --- #
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
