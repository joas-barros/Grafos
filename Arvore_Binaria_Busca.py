from Arvore_Binaria import No

class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None

    def getraiz(self):
        return self.raiz

    def insere(self, valor):
        no = No(valor)
        if self.raiz is None:
            self.raiz = no
        else:
            no_atual = self.raiz
            no_pai = None
            while True:
                if no_atual is not None:
                    no_pai = no_atual
                    if no.getvalor() < no_atual.getvalor():
                        no_atual = no_atual.getesquerda()
                    else:
                        no_atual = no_atual.getdireita()
                else:
                    if no.getvalor() < no_pai.getvalor():
                        no_pai.setesquerda(no)
                    else:
                        no_pai.setdireita(no)
                    break

    def mostraarvore(self, no_atual):
        if no_atual is not None:
            self.mostraarvore(no_atual.getesquerda())
            print(f'{no_atual.getvalor()}', end=' ')
            self.mostraarvore(no_atual.getdireita())


if __name__ == '__main__':
    t = ArvoreBinariaBusca()

    lista = [8, 3, 6, 10, 14, 1, 7, 13, 4]
    for i in lista:
        t.insere(i)

    t.mostraarvore(t.getraiz())
