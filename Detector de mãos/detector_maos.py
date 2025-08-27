# --- Importar as bibliotecas --- #
import cv2
import mediapipe as mp


class DetectorMaos:
    """Classe responsável pela detecção das mãos."""
    def __init__(self, modo=False, max_maos=2, deteccao_confianca=0.5,
                 rastreio_confianca=0.5, cor_pontos=(0, 0, 255), cor_conexoes=(255, 255, 255)):
        """
        Função responsável por inicializar a classe.
        :param modo: Modo da captura da imagem. Se True, a detecção e rastreio serão feitos a todo momento;
        deixa muito travado. Se False, não são feitas a detecção e rastreio a todo momento; pode perder por
        alguns instântes as marcações, porém não trava.
        :param max_maos: Quantidade máxima de mãos para serem detectadas.
        :param deteccao_confianca: Percentual da taxa de detecção da mão. Se for menor do que este liminte,
        a detecção não ocorre.
        :param rastreio_confianca: Percentual da taxa de rastreio dos pontos da mão. Se for menor que este
        limite, o rastreio dos pontos não é realizado.
        :param cor_pontos: Cor dos pontos.
        :param cor_conexoes: Cor das conexões.
        """
        # --- Inicializar os parâmetros --- #
        self.modo = modo
        self.max_maos = max_maos
        self.deteccao_confianca = deteccao_confianca
        self.rastreio_confianca = rastreio_confianca
        self.cor_pontos = cor_pontos
        self.cor_conexoes = cor_conexoes

        # --- Inicializar os módulos de detecção das mãos --- #
        self.maos_mp = mp.solutions.hands
        self.maos = self.maos_mp.Hands(
            self.modo,
            self.max_maos,
            1,
            self.deteccao_confianca,
            self.rastreio_confianca
        )

        # --- Função para desenhar os pontos nas mãos --- #
        self.desenho_mp = mp.solutions.drawing_utils

        # --- Configurações do desenho dos pontos --- #
        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(color=self.cor_pontos)

        # --- Configurações do desenho das conexões --- #
        self.desenho_config_conexoes = self.desenho_mp.DrawingSpec(color=self.cor_conexoes)

    def encontrar_maos(self, imagem, desenho=True):
        """
        Função responsável por detectar a(s) mão(s).
        :param imagem: Imagem capturada.
        :param desenho: Desenhar os pontos e as conexões na(s) mão(s).
        :return: Retorna a imagem com a detecção.
        """
        # --- Converter a imagem de BGR para RGB --- #
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

        # --- Passar a imagem convertida para o detector --- #
        self.resultado = self.maos.process(imagem_rgb)

        # --- Verificar se alguma mão foi detectada --- #
        if self.resultado.multi_hand_landmarks:
            for pontos in self.resultado.multi_hand_landmarks:
                if desenho:
                    # --- Desenhar os pontos nas mãos detectadas --- #
                    self.desenho_mp.draw_landmarks(
                        imagem,  # imagem de captura
                        pontos,  # pontos da mão
                        self.maos_mp.HAND_CONNECTIONS,  # conexão entre os pontos
                        self.desenho_config_pontos,  # cor dos pontos
                        self.desenho_config_conexoes  # cor das conexões
                    )

        return imagem

    def encontrar_pontos(self, imagem, mao_num=0, desenho=True, cor=(255, 0, 255), raio=7, ponto_detectado=0):
        """
        Função responsável por encontrar a posição dos pontos da(s) mão(s).
        :param imagem: Imagem capturada.
        :param mao_num: Número da mão detectada.
        :param desenho: Desenhar o ponto encontrado.
        :param cor: Tupla com a cor do ponto (BGR).
        :param raio: Raio do círculo do ponto.
        :param ponto_detectado: Ponto a ser detectado.
        :return: Lista com os pontos detectados.
        """
        # --- Lista com os pontos detectados --- #
        lista_pontos = []

        # --- Verificar se alguma mão foi detectada --- #
        if self.resultado.multi_hand_landmarks:
            # --- Obter os pontos da mão detectada, não de todas --- #
            mao = self.resultado.multi_hand_landmarks[mao_num]

            # --- Obter as informações dos pontos --- #
            for id, ponto in enumerate(mao.landmark):
                if id == ponto_detectado:
                    # --- Obter as dimenões da imagem capturada --- #
                    altura, largura, _ = imagem.shape

                    # --- Transformar a posição do ponto de proporção para pixel --- #
                    centro_x, centro_y = int(ponto.x * largura), int(ponto.y * altura)

                    # --- Adicionar os pontos da mão detectada na lista --- #
                    lista_pontos.append([id, centro_x, centro_y])

                    # --- Colocar um círculo em um ponto --- #
                    if desenho:
                        cv2.circle(
                            imagem,  # imagem da captura
                            (centro_x, centro_y),  # centro do círculo
                            raio,  # raio do círculo
                            cor,  # cor do círculo
                            cv2.FILLED  # espessura
                        )

        return lista_pontos


def main():
    # --- Capturar o vídeo pela webcam --- #
    cap = cv2.VideoCapture(0)

    # --- Instanciar a classe do detector --- #
    detector = DetectorMaos()

    # --- Realizar a captura --- #
    while True:
        # --- Obter a imagem --- #
        _, imagem = cap.read()

        # --- Inverter a imagem --- #
        imagem = cv2.flip(imagem, 1)

        # --- Realizar a detecção das mãos --- #
        imagem = detector.encontrar_maos(imagem)

        # --- Lista com os pontos --- #
        lista_pontos = detector.encontrar_pontos(imagem)

        # --- Mostrar a imagem de captura --- #
        cv2.imshow('Captura', imagem)

        # --- Tempo de atualização da captura --- #
        cv2.waitKey(1)


if __name__ == '__main__':
    main()

