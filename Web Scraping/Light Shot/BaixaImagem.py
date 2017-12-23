from requests import get
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

def download(url, nomeDoArquivo):

    response = get(url)

    img = np.array(Image.open(BytesIO(response.content)))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    h1 = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_eye.xml')
    h2 = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_eye_tree_eyeglasses.xml')
    h3 = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_frontalface_alt.xml')
    h4 = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_fullbody.xml')
    h5 = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_profileface.xml')
    h6 = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_upperbody.xml')

    r1 = h1.detectMultiScale(gray, 1.3, 5)
    r2 = h2.detectMultiScale(gray, 1.3, 5)
    r3 = h3.detectMultiScale(gray, 1.3, 5)
    r4 = h4.detectMultiScale(gray, 1.3, 5)
    r5 = h5.detectMultiScale(gray, 1.3, 5)
    r6 = h6.detectMultiScale(gray, 1.3, 5)

    arq = ''

    #Filtra Imagens conforme haarcascade
    if(len(r5) > 0 or len(r3) > 0 or len(r4) > 0 or len(r1) > 0 or len(r2) > 0 or len(r6) > 0):
        arq = 'imagens/rosto/' + nomeDoArquivo + '.png'
    else:
        arq = 'imagens/' + nomeDoArquivo + '.png'
    with open(arq, 'wb') as arquivo:
        # Grava arquivo
        arquivo.write(response.content)
