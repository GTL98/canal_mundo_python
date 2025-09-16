# --- Importar as bibliotecas --- #
import cv2
import mediapipe as mp


class DetectorRosto:
    """Classe responsável por detectar rostos."""
    def __init__(self, deteccao_confianca=0.5):
        """
        Função responsável por inicializar a classe.
        :param deteccao_confianca: Percentual da taxa de detecção do rosto. Se for menor do que este limite,
        a detecção não ocorre.
        """
        # --- Inicializar o parâmetro --- #
        self.deteccao_confianca = deteccao_confianca

        # --- Inicializar a função de detecção do rosto --- #
        self.rosto_mp = mp.solutions.face_detection
        self.rosto = self.rosto_mp.FaceDetection(self.deteccao_confianca)

    def encontrar_rosto(
            self,
            imagem,
            desenho=True,
            cor_caixa=(255, 0, 255),
            cor_moldura=(255, 0, 255),
            comprimento=30,
            espessura_moldura=5,
            espessura_retangulo=1,
            desenho_caixa=True,
            desenho_moldura=True
    ):
        """
        Função responsável por detectar o(s) rosto(s).
        :param imagem: Imagem capturada.
        :param desenho: Desenhar a(s) caixa(s) de detecção do(s) rosto(s).
        :param cor_caixa: Cor da caixa.
        :param cor_moldura: Cor da moldura.
        :param comprimento: Comprimento da linha da moldura.
        :param espessura_moldura: Espessura da linha da moldura.
        :param espessura_retangulo: Espessura do retângulo da(s) caixa(s).
        :param desenho_caixa: Desenhar a caixa de detecção.
        :param desenho_moldura: Desenhar a moldura na caixa de detecção.
        :return: Retorna a imagem com a detecção e a lista com a(s) caixa(s) de detecção.
        """
        # --- Converter a imagem de BGR para RGB --- #
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

        # --- Passar a imagem convertida para o detector --- #
        resultado = self.rosto.process(imagem_rgb)

        # --- Lista com as caixas de detecção do(s) rosto(s) --- #
        caixas = []

        # --- Verificar se ocorreu a detecção do rosto --- #
        if resultado.detections:
            # --- Obter o ID da detecção, bem como a detecção --- #
            for id, deteccao in enumerate(resultado.detections):
                # --- Informações da caixa de reconhecimento --- #
                info_caixa = deteccao.location_data.relative_bounding_box

                # --- Dimensões da imagem de captura --- #
                altura, largura, _ = imagem.shape

                # --- Caixa de detecção --- #
                caixa = (int(info_caixa.xmin * largura), int(info_caixa.ymin * altura),
                         int(info_caixa.width * largura), int(info_caixa.height * altura))

                # --- Adicionar a caixa à lista de caixas --- #
                caixas.append([id, caixa, deteccao.score])

                # --- Desenhar a caixa em volta do rosto detectado --- #
                if desenho:
                    imagem = self.desenho_moldura(
                        imagem,
                        caixa,
                        cor_caixa,
                        cor_moldura,
                        comprimento,
                        espessura_moldura,
                        espessura_retangulo,
                        desenho_caixa,
                        desenho_moldura
                    )

                    # --- Colocar na caixa de detecção a porcentagem de certeza da detecção --- #
                    cv2.putText(
                        imagem,  # imagem capturada
                        f'{int(deteccao.score[0] * 100)}%',  # texto
                        (caixa[0], caixa[1] - 20),  # posição do texto
                        cv2.FONT_HERSHEY_PLAIN,  # fonte
                        2,  # tamanho da fonte
                        (255, 0, 255),  # cor da fonte
                        2  # espessura
                    )

        return imagem, caixas

    def desenho_moldura(
            self,
            imagem,
            caixa,
            cor_caixa,
            cor_moldura,
            comprimento,
            espessura_moldura,
            espessura_retangulo,
            desenho_caixa,
            desenho_moldura
    ):
        """
        :param imagem: Imagem capturada.
        :param caixa: Caixa de detecção.
        :param cor_caixa: Cor da caixa.
        :param cor_moldura: Cor da moldura.
        :param comprimento: Comprimento da linha da moldura.
        :param espessura_moldura: Espessura da linha da moldura.
        :param espessura_retangulo: Espessura do retângulo da(s) caixa(s).
        :param desenho_caixa: Desenhar a caixa de detecção.
        :param desenho_moldura: Desenhar a moldura na caixa de detecção.
        :return: Retorna a imagem com a detecção.
        """
        # --- Dimensões da caixa --- #
        x, y, largura, altura = caixa

        # --- Pontos iniciais da moldura --- #
        x_1, y_1 = x + largura, y + largura

        if desenho_caixa:
            # --- Desenhar a caixa em volta do rosto detectado --- #
            cv2.rectangle(
                imagem,  # imagem capturada
                caixa,  # pontos da caixa
                cor_caixa,  # cor do retângulo
                espessura_retangulo  # espessura da linha do retângulo
            )

        if desenho_moldura:
            # --- Canto superior esquerdo --- #
            cv2.line(
                imagem,  # imagem capturada
                (x, y),  # ponto inicial
                (x + comprimento, y),  # ponto final
                cor_moldura,  # cor da moldura
                espessura_moldura  # espessura da moldura
            )
            cv2.line(
                imagem,
                (x, y),
                (x, y + comprimento),
                cor_moldura,
                espessura_moldura
            )

            # --- Canto superior direito --- #
            cv2.line(
                imagem,
                (x_1, y),
                (x_1 - comprimento, y),
                cor_moldura,
                espessura_moldura
            )
            cv2.line(
                imagem,
                (x_1, y),
                (x_1, y + comprimento),
                cor_moldura,
                espessura_moldura
            )

            # --- Canto inferior esquerdo --- #
            cv2.line(
                imagem,
                (x, y_1),
                (x + comprimento, y_1),
                cor_moldura,
                espessura_moldura
            )
            cv2.line(
                imagem,
                (x, y_1),
                (x, y_1 - comprimento),
                cor_moldura,
                espessura_moldura
            )

            # --- Canto inferior direito --- #
            cv2.line(
                imagem,
                (x_1, y_1),
                (x_1 - comprimento, y_1),
                cor_moldura,
                espessura_moldura
            )
            cv2.line(
                imagem,
                (x_1, y_1),
                (x_1, y_1 - comprimento),
                cor_moldura,
                espessura_moldura
            )

        return imagem


def main():
    # --- Captura da webcam --- #
    cap = cv2.VideoCapture(0)

    # --- Instanciar o detector de rosto --- #
    detector = DetectorRosto()

    # --- Loop de captura --- #
    while True:
        # --- Obter a imagem --- #
        _, imagem = cap.read()

        # --- Inverter a imagem --- #
        imagem = cv2.flip(imagem, 1)

        # --- Derectar o rosto --- #
        imagem, caixas = detector.encontrar_rosto(imagem)

        # --- Mostrar a captura --- #
        cv2.imshow('Detector de rosto', imagem)

        # --- Tempo de atualização da captura --- #
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
