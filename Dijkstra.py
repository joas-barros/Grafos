from HeapMinimo import Heapmin


class Grafos:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafos = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafos[u - 1][v - 1] = peso
        self.grafos[v - 1][u - 1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacencia é:')
        for i in range(self.vertices):
            print(self.grafos[i])

    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = HeapminDijkstra()
        h.adiciona_no(0, origem)
        while h.quant_nos() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafos[v - 1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafos[v - 1][i]:
                        custo_vem[i] = [dist + self.grafos[v - 1][i], v]
                        h.adiciona_no(dist + self.grafos[v - 1][i], i + 1)
        return custo_vem


class HeapminDijkstra(Heapmin):
    def __init__(self):
        super().__init__()
        self.heap = []
        self.nos = 0

    def adiciona_no(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        filho = self.nos
        while True:
            if filho == 1:
                break
            pai = filho // 2
            if self.heap[pai - 1][0] <= self.heap[filho - 1][0]:
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
                if self.heap[filho][0] < self.heap[filho - 1][0]: # < se for minimo
                    filho += 1
            if self.heap[pai - 1][0] <= self.heap[filho - 1][0]:
                break
            else:
                self.heap[filho - 1], self.heap[pai - 1] = self.heap[pai - 1], self.heap[filho - 1]
                pai = filho
        return x


if __name__ == '__main__':
    g = Grafos(7)

    g.adiciona_aresta(1, 2, 5)
    g.adiciona_aresta(1, 3, 6)
    g.adiciona_aresta(1, 4, 10)
    g.adiciona_aresta(2, 5, 13)
    g.adiciona_aresta(3, 4, 3)
    g.adiciona_aresta(3, 5, 11)
    g.adiciona_aresta(3, 6, 6)
    g.adiciona_aresta(4, 5, 6)
    g.adiciona_aresta(4, 6, 4)
    g.adiciona_aresta(5, 7, 3)
    g.adiciona_aresta(6, 7, 8)

    g.mostra_matriz()
    resultado = g.dijkstra(1)
    print(resultado)
