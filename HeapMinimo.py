from HeapMaximo import Heapmax


class Heapmin(Heapmax):
    def __init__(self):
        super().__init__()
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
            if self.heap[pai - 1] <= self.heap[filho - 1]:
                break
            else:
                self.heap[pai - 1], self.heap[filho - 1] = self.heap[filho - 1], self.heap[pai - 1]
                filho = pai


if __name__ == '__main__':
    lista = [17, 36, 25, 7, 3, 100, 1, 2, 19]
    print('heap minimo')
    hmin = Heapmin()
    hmin.ordenar(lista)
    hmin.mostra_heap()
