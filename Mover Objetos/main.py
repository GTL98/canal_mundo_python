# --- Importar as bibliotecas --- #
import cv2
import numpy as np
from mpvc import DetectorMaos
from criar_quadrado import Quadrado

# --- Capturar a webcam --- #
cap = cv2.VideoCapture(0)

# --- Alterar a dimensão da tela de captura --- #
cap.set(3, 1280)
cap.set(4, 720)

# --- Detector de mãos --- #
detector = DetectorMaos(deteccao_confianca=0.8)

# --- Criar os quadrados --- #
cor = (125, 125, 125)
quadrados = [Quadrado([i*250+150, 150]) for i in range(5)]

# --- Loop de captura --- #
while True:
    # --- Obter a imagem de captura --- #
    _, imagem = cap.read()

    # --- Inverter a imagem --- #
    imagem = cv2.flip(imagem, 1)

    # --- Encontrar as mãos --- #
    imagem = detector.encontrar_maos(imagem)

    # --- Encontrar o ponto para ser o cursor --- #
    cursor = detector.encontrar_pontos(imagem, ponto_detectado=8, desenho=False)

    # --- Verificar se o cursor está na área do quadrado --- #
    if cursor:
        # --- Encontrar a distância entre os pontos --- #
        distancia, _, _ = detector.encontrar_distancia(8, 12, imagem, desenho_linha=False, desenho_ponto=False)
        if distancia < 45:
            for quadrado in quadrados:
                quadrado.atualizar(cursor)

    # --- Criar os quadrados --- #
    imagem_nova = np.zeros_like(imagem, np.uint8)
    for quadrado in quadrados:
        cx, cy = quadrado.posicao_centro
        a, l = quadrado.tamanho
        cv2.rectangle(
            imagem_nova,
            (cx - l // 2, cy - a // 2),
            (cx + l // 2, cy + a // 2),
            cor,
            cv2.FILLED
        )
    saida = imagem.copy()
    alfa = 0.5
    mascara = imagem_nova.astype(bool)
    saida[mascara] = cv2.addWeighted(imagem, alfa, imagem_nova, 1 - alfa, 0)[mascara]

    # --- Mostrar a imagem --- #
    cv2.imshow('Captura', saida)

    # --- Delay de captura --- #
    cv2.waitKey(1)