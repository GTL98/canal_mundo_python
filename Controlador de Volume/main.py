# --- Importar as bibliotecas --- #
import cv2
import numpy as np
from mpvc import DetectorMaos
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# --- Capturar da webcam --- #
cap = cv2.VideoCapture(0)

# --- Instanciar o detector --- #
detector = DetectorMaos(max_maos=1, deteccao_confianca=0.7)

# --- Obter o volume dos speakers --- #
aparelhos = AudioUtilities.GetSpeakers()
volume = aparelhos.EndpointVolume

while True:
    # --- Obter a imagem capturada --- #
    _, imagem = cap.read()

    # --- Detectar a mão --- #
    imagem = detector.encontrar_maos(imagem)

    # --- Obter a distância entre os pontos --- #
    distancia, imagem, _ = detector.encontrar_distancia(4, 8, imagem)

    # --- Converter a distância para o intervalo do volume --- #
    vol = np.interp(
        distancia,  # distância entre os pontos
        [20, 160],  # mínimo e máximo da distância entre os pontos
        [0, 1]
    )

    # --- Converter o valor da barra --- #
    vol_barra = np.interp(
        distancia,
        [20, 160],
        [400, 100]
    )

    # --- Converter a distância para porcentagem --- #
    vol_porc = np.interp(
        distancia,
        [20, 160],
        [0, 100]
    )

    # --- Alterar o volume --- #
    volume.SetMasterVolumeLevelScalar(vol, None)

    # --- Barra para o controle do volume --- #
    cv2.rectangle(
        imagem,
        (50, 100),  # pontos iniciais
        (85, 400),  # pontos finais
        (167, 59, 93),  # cor
        3  # espessura
    )
    cv2.rectangle(
        imagem,
        (50, int(vol_barra)),
        (85, 400),
        (0, 255, 0),
        cv2.FILLED
    )

    # --- Colocar a porcentagem do volume --- #
    cv2.putText(
        imagem,
        f'{int(vol_porc)}%',  # texto
        (40, 450),  # posição
        cv2.FONT_HERSHEY_COMPLEX,  # fonte
        1,  # tamanho da fonte
        (0, 0, 255),  # cor
        3,  # espessura
    )

    # --- Mostrar a imagem --- #
    cv2.imshow('Captura', imagem)

    # --- Delay de captura --- #
    cv2.waitKey(1)