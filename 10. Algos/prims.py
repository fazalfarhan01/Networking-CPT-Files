import sys  # Library for INT_MAX
from common import clear, custom_print
from terminaltables import SingleTable


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        clear()
        self.printGraph()
        data = [["Start Edge", "End Edge", "Weight"]] + [[parent[i],
                                                          i, self.graph[i][parent[i]]] for i in range(1, self.V)]
        table = SingleTable(data)
        table.inner_row_border = True
        print(table.table)

    def printFinalDistances(self, src, dist):
        clear()
        self.printGraph()
        sourceInfo = ["Source"], [src]
        sourceTable = SingleTable(sourceInfo)
        print(sourceTable.table)

        data = ["Vertex"]+list(range(self.V)), ["Distance from source"]+dist
        table = SingleTable(data)
        print(table.table)

    def printGraph(self):
        table = SingleTable(self.graph)
        table.inner_row_border = True
        print(table.table)

    def minKey(self, key, mstSet):

        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self, src):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = src
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
# ]

g.primMST(2)
