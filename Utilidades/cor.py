import random

COR_PRETA = (0,0,0)
COR_BRANCA = (255,255,255)
COR_VERMELHA = (191,0,0)
COR_VERDE = (0,191,0)
COR_AZUL = (0,0,191)

def randCor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def randCorEscura():
    return (random.randint(0,128),random.randint(0,128),random.randint(0,128))

def randCorMedia():
    return (random.randint(64,193),random.randint(64,193),random.randint(64,193))

def randCorClara():
    return (random.randint(127,255),random.randint(127,255),random.randint(127,255))

def randCorBonita():
    rgb = [0, 1, 2]

    cor1 = int(random.choice(rgb))
    rgb.remove(cor1)
    cor2 = int(random.choice(rgb))
    rgb.remove(cor2)
    cor3 = rgb[0]

    rgb = [0, 0, 0]

    rgb[cor1] = 191
    rgb[cor2] = random.randint(0,191)
    rgb[cor3] = 0
    return (rgb[0],rgb[1],rgb[2])

def inverterCor(rgb=tuple):
    return (255-rgb[0],255-rgb[1],255-rgb[2])

def clarear(rgb=tuple, qnt=10):
    r = rgb[0] + qnt
    g = rgb[1] + qnt
    b = rgb[2] + qnt

    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b =255

    return (r,g,b)

def escurecer(rgb=tuple, qnt=10):
    r = rgb[0] - qnt
    g = rgb[1] - qnt
    b = rgb[2] - qnt

    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0

    return (r,g,b)

if __name__ == "__main__":
    input("Modulo de cores RGB!")
