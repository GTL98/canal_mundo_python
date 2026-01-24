# --- Importar as bibliotecas --- #
import cv2
from cvzone.FaceDetectionModule import FaceDetector

# --- Ligar a webcam --- #
cap = cv2.VideoCapture(0)

# --- Redimensiozar a tela de captura --- #
cap.set(3, 640)
cap.set(4, 480)

# --- Criar o detector --- #
detector = FaceDetector(minDetectionCon=0.75)

while True:
    # --- Obter a caputra --- #
    _, imagem = cap.read()

    # --- Inverter a imagem --- #
    imagem = cv2.flip(imagem, 1)

    # --- Encontrar o rosto --- #
    imagem, bboxes = detector.findFaces(imagem, draw=False)

    # --- Verificar se algum rosto foi detectado --- #
    if bboxes:
        for i, bbox in enumerate(bboxes):
            # --- Obter as dimensões do quadro em volto do rosto --- #
            x, y, l, a = bbox['bbox']

            # --- Evitar que o programa pare de funcionar devido a proximidade com a câmera --- #
            if x < 0:
                x = 0
            if y < 0:
                y = 0

            # --- Cortar a imagem em volta do rosto --- #
            imagem_cortada = imagem[y:y+a, x:x+a]

            # --- Gerar o blur --- #
            imagem_blur = cv2.blur(imagem_cortada, (35, 35))

            # --- Colocar o blur na imagem de captura --- #
            imagem[y:y+a, x:x+a] = imagem_blur

    # --- Mostrar a captura --- #
    cv2.imshow('Face Blur', imagem)

    # --- Intervalo de leitura --- #
    cv2.waitKey(1)
