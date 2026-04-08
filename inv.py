import numpy as np
import cv2 as cv

if __name__ == "__main__":
    # Você está tentando processar multiplos raio-x para detectar anomalias. Infelizmente alguns raio-x não estão no formato certo para deixar sua pesquisa fácil.
    # Geralmente raio-x usam as cores mais escuras para representar as áreas menos densas da imagem, enquanto as cores claras representam áreas de alta densidade, como ossos.
    # Transforme a imagem xray-inverted.jpg para que siga o mesmo padrão, ossos brancos e fundo preto, em vez da estrutura atual.

    # Inverter a cor dos ossos de cinza para branco e o fundo de branco para preto
    img = cv.imread('img/xray-inverted.jpg')
    height, width, _ = img.shape

    # invert color from the image: white - darker color = whiter color
    img = 255 - img
    cv.imwrite("img/xray.jpg", img)