# --- Importar as bibliotecas --- #
import cv2
import imutils
import numpy as np

# --- Abrir a imagem --- #
imagem = cv2.imread('./imagens/1.jpg')

# --- Redimenzionar a imagem --- #
imagem = imutils.resize(imagem, width=640)

# --- Converter os canais da imagem --- #
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagem_cinza = cv2.cvtColor(imagem_cinza, cv2.COLOR_GRAY2BGR)
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# --- Intervalo da cor --- #
limite_inferior = np.array([90, 50, 0])
limite_superior = np.array([145, 255, 255])

# --- Criar a máscara --- #
mascara = cv2.inRange(imagem_hsv, limite_inferior, limite_superior)
mascara = cv2.medianBlur(mascara, 7)

# --- Colocar a cor detectada na máscara --- #
cor_detectada = cv2.bitwise_and(imagem, imagem, mask=mascara)

# --- Inverter a máscara --- #
mascara_invertida = cv2.bitwise_not(mascara)

# --- Restante da imagem em cinza --- #
cinza = cv2.bitwise_and(imagem_cinza, imagem_cinza, mask=mascara_invertida)

# --- Juntar a imagem cinza com a máscara --- #
imagem_final = cv2.add(cinza, cor_detectada)

# --- Mostrar a imagem --- #
cv2.imshow('Imagem', imagem)
cv2.imshow('Imagem final', imagem_final)
cv2.imwrite('imagem_final.png', imagem_final)
cv2.waitKey(0)