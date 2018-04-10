import os

def dirExite(caminho):
    diretorio = os.path.dirname(caminho)
    if not os.path.exists(diretorio):
        return False
    else:
        return True

def dirCria(caminho):
    diretorio = os.path.dirname(caminho)
    if not os.path.exists(diretorio):
        os.mkdir(caminho)
        return True
    else:
        return False
