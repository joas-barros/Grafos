from math import log2


class Heapmax:
    def __init__(self):
        self.heap = []
        self.nos = 0

    def adiciona_no(self, u):
        self.heap.append(u)
        self.nos += 1
        filho = self.nos
        while True:
            if filho == 1:
                break
            pai = filho // 2
            if self.heap[pai - 1] >= self.heap[filho - 1]:
                break
            else:
                self.heap[pai - 1], self.heap[filho - 1] = self.heap[filho - 1], self.heap[pai - 1]
                filho = pai

    def ordenar(self, lista):
        for i in lista:
            self.adiciona_no(i)

    def mostra_heap(self):
        print('A estrutura heap é a seguinte:')
        nivel = int(log2(self.nos))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end='  ')
                a += 1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end='  ')
            a += 1
        print()

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        pai = 1
        while True:
            # filho a esquerda
            filho = 2 * pai
            if filho > self.nos:
                break
            if filho + 1 <= self.nos:
                if self.heap[filho] > self.heap[filho - 1]: # < se for minimo
                    filho += 1
            if self.heap[pai - 1] >= self.heap[filho - 1]:
                break
            else:
                self.heap[filho - 1], self.heap[pai - 1] = self.heap[pai - 1], self.heap[filho - 1]
                pai = filho
        return x

    def quant_nos(self):
        return self.nos

    def tamanho(self):
        t = log2(self.nos)
        if t == int(t):
            return t + 1
        else:
            return int(t) + 1

    def elemento_raiz(self):
        if self.nos != 0:
            return self.heap[0]
        return 'A árvore está vazia'

    def __posicao(self, elem):
        for i in range(len(self.heap)):
            if self.heap[i] == elem:
                return i + 1

    def filho_esquerda(self, elem):
        i = self.__posicao(elem)
        if self.nos >= 2 * i:
            return self.heap[2 * i - 1]
        return 'Esse nó não tem filho a esquerda'

    def filho_direita(self, elem):
        i = self.__posicao(elem)
        if self.nos >= 2 * i + 1:
            return self.heap[2 * i]
        return 'Esse nó não tem filho a direita'

    def pai(self, elem):
        i = self.__posicao(elem)
        return self.heap[i // 2]


if __name__ == '__main__':
    lista = [17, 36, 25, 7, 3, 100, 1, 2, 19]
    print('heap maximo')
    h = Heapmax()
    h.ordenar(lista)
    raiz = h.remove_no()
    print(f'A raiz é: {raiz}')
    h.mostra_heap()

    print(f'Tamanho = {h.tamanho()}')
    print(f'nos = {h.quant_nos()}')
    print(f'Filho a esquerda de 17 = {h.filho_esquerda(17)}')
    print(f'Filho a direita de 17 = {h.filho_direita(17)}')


