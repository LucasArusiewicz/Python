import cv2
import numpy as np
from urllib.request import Request, urlopen

#Pagina que retorna imagem da camera
#Utilizado DroidCam para testes
link = 'http://192.168.0.2:4747/cam/1/frame.jpg'
req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})

while True:
    cama = np.array(bytearray(urlopen(req).read()), dtype=np.uint8)
    img = cv2.imdecode(cama, 1)
    cv2.imshow('camera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
