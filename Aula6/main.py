import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('imagem.jpg')
imagem2 = cv2.imread('imagem2.jpg')

# Definir a matriz de translação
tx, ty = 100, 50
matriz_translacao = np.float32([[0, 1, tx], [1, 0, ty]])

# Aplicar a translação
imagem_transladada = cv2.warpAffine(imagem, matriz_translacao, (imagem.shape[1], imagem.shape[0]))
imagem_transladada2 = cv2.warpAffine(imagem2, matriz_translacao, (imagem2.shape[1], imagem2.shape[0]))

# Exibir resultado
cv2.imshow('Imagem Transladada 1', imagem_transladada)
cv2.waitKey(0)

cv2.imshow('Imagem Transladada 2', imagem_transladada2)
cv2.waitKey(0)

cv2.destroyAllWindows()

