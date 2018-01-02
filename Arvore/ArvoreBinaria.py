class No:
    def __init__(self, dado):
        self._dado = dado
        self._filhoE = None
        self._filhoD = None
        self._pai = None

    def getDado(self):
        return self._dado

    def setDado(self, novo):
        self._dado = novo

    def getFilhoE(self):
        return self._filhoE

    def setFilhoE(self, filho):
        self._filhoE = filho

    def getFilhoD(self):
        return self._filhoD

    def setFilhoD(self, filho):
        self._filhoD = filho

    def getPai(self):
        return self._pai

    def setPai(self, pai):
        self._pai = pai

    def __str__(self):
        return str("No: {}".format(self._dado))

class ArvoresBinaria(No):
    def __init__(self):
        self._raiz = None

    def getRaiz(self):
        return self._raiz

    def setRaiz(self, nova):
        self._raiz = nova

    def Buscar(self, raiz, dado):
        if(raiz == None or raiz.getDado() == dado):
            return raiz
        if(dado < raiz.getDado()):
            return self.Buscar(raiz.getFilhoE(), dado)
        else:
            return self.Buscar(raiz.getFilhoD(), dado)

    def minimo(self, noRaiz):
        while noRaiz.getFilhoE() is None:
            noRaiz = noRaiz.getFilhoD()
        return noRaiz

    def maximo(self, noRaiz):
        while noRaiz.getFilhoD() is None:
            noRaiz = noRaiz.getFilhoE()
        return noRaiz

    def sucessor(self, noRaiz):
        if(noRaiz.getFilhoD() != None):
            return self.minimo(noRaiz.getFilhoD())
        pai = noRaiz.getPai()
        while pai != None and noRaiz is pai.getFilhoD():
            noRaiz = pai
            pai = pai.getPai()
        return pai

    def antecessor(self, noRaiz):
        if (noRaiz.getFilhoE() != None):
            return self.maximo(noRaiz.getFilhoE())
        pai = noRaiz.getPai()
        while pai != None and noRaiz is pai.getFilhoE():
            noRaiz = pai
            pai = pai.getPai()
        return pai

    def Inserir(self, novoNo):
        pai = None
        raiz = self.getRaiz()
        while raiz != None:
            pai = raiz
            if(novoNo.getDado() < raiz.getDado()):
                raiz = raiz.getFilhoE()
            else:
                raiz = raiz.getFilhoD()
        novoNo.setPai(pai)
        if(pai == None):
            self.setRaiz(novoNo)
        else:
            if(novoNo.getDado() < pai.getDado()):
                pai.setFilhoE(novoNo)
            else:
                pai.setFilhoD(novoNo)

    def Remover(self, no):
        if(no.getFilhoE() == None or no.getFilhoD() == None):
            suces = no
        else:
            suces = self.sucessor(no)

        if(suces.getFilhoE() != None):
            filhoSuces = suces.getFilhoE()
        else:
            filhoSuces = suces.getFilhoD()

        if(filhoSuces != None):
            filhoSuces.setPai(suces.getPai())

        if(suces.getPai() == None):
            self.setRaiz(filhoSuces)
        else:
            if(suces == suces.getPai().getFilhoE()):
                suces.getPai().setFIlhoE(filhoSuces)
            else:
                suces.getPai().setFIlhoD(filhoSuces)
        if(suces != no):
            no.setDado(suces.getDado())
