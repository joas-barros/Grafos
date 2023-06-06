class no:

    def __int__(self, valor):
        self.valor = valor
        self.proximo = None

    def getvalor(self):
        return self.valor

    def setproximo(self, proximo):
        self.proximo = proximo

    def getproximo(self):
        return self.proximo


if __name__ == '__main__':
    no1 = no(4)
    no2 = no(2)

    print(no1.getvalor())
    print(no2.getvalor())

