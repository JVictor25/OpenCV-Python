import numpy as np
import cv2

def showImage(img):
    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img, y , x):
     return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
        img[y, x, 0] = b
        img[y, x, 1] = g
        img[y, x, 2] = r
def main():
    objetoImagem = cv2.imread("imgs/simba1.jpeg")
    print(objetoImagem.shape)
    altura, largura, canaisDeCor = objetoImagem.shape
    print("Dimensões da Imagem: " + str(altura) + ", " + str(largura))
    print("Canais de cor: " + str(canaisDeCor))   
    
    for y in range(0, altura):
        for x in range(0, largura):
            #azul = objetoImagem.item(y, x, 0)
            #verde = objetoImagem.item(y, x, 1)
            #vermelho = objetoImagem.item(y, x, 2)

            #objetoImagem[y, x, 0] = 0  
            #objetoImagem[y, x, 1] = 0  
            #objetoImagem[y, x, 2] = 0 
            azul, verde, vermelho = getColor(objetoImagem, y, x)
            #setColor(objetoImagem, x, y, verde, vermelho, azul)

    #objetoImagemOlho=objetoImagem[851:851 + 50, 762:762+60]
    #objetoImagem[931:931+objetoImagemOlho.shape[0],630:630+objetoImagemOlho.shape[1]]=objetoImagemOlho
    #showImage(objetoImagemOlho)
    #cv2.imwrite("imgs/simbaModificado.png", objetoImagem)
    showImage(objetoImagem)

main()
