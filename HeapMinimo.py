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
                if self.heap[filho] < self.heap[filho - 1]: # < se for minimo
                    filho += 1
            if self.heap[pai - 1] <= self.heap[filho - 1]:
                break
            else:
                self.heap[filho - 1], self.heap[pai - 1] = self.heap[pai - 1], self.heap[filho - 1]
                pai = filho
        return x


if __name__ == '__main__':
    lista = [17, 36, 25, 7, 3, 100, 1, 2, 19]
    print('heap minimo')
    hmin = Heapmin()
    hmin.ordenar(lista)
    raiz = hmin.remove_no()
    print(f'raiz = {raiz}')
    hmin.mostra_heap()

    print(f'Tamanho = {hmin.tamanho()}')
    print(f'nos = {hmin.nos}')
    print(f'Filho a esquerda de 2 = {hmin.filho_esquerda(2)}')
    print(f'Filho a direita de 2 = {hmin.filho_direita(2)}')
