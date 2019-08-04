import cv2
import numpy as np

img = cv2.imread("challenge_strider.png")

vermelho_claro = np.array([0, 0, 130], np.uint8)
vermelho_escuro = np.array([0, 0, 255], np.uint8)

imagem = cv2.inRange(img, vermelho_claro, vermelho_escuro)
resultado = cv2.countNonZero(imagem)
print('Número de pixels vermelhos: ' + str(resultado))

cv2.waitKey(0)
