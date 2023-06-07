class No:

    def __int__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def getvalor(self):
        return self.valor

    def setesquerda(self, esquerda):
        self.esquerda = esquerda

    def setdireita(self, direita):
        self.direita = direita

    def getesquerda(self):
        return self.esquerda

    def getdireita(self):
        return self.direita
