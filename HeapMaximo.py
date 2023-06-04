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


if __name__ == '__main__':
    lista = [17, 36, 25, 7, 3, 100, 1, 2, 19]
    print('heap maximo')
    h = Heapmax()
    h.ordenar(lista)
    h.mostra_heap()


