from terminaltables import SingleTable
from common import clear


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimumCost = 0
        clear()
        print("Edges in the constructed MST")
        data = [["Edge 1", "Edge 2", "Weight"]]
        for u, v, weight in result:
            minimumCost += weight
            data.append([u, v, weight])
        table = SingleTable(data)
        table.inner_row_border = True
        print(table.table)
        print(SingleTable([["Minimum Spanning Tree", minimumCost]]).table)


clear()
# number_of_nodes = int(input("Enter the number of nodes: "))
# number_of_edges = int(input("Enter the number of edges: "))
# g = Graph(number_of_nodes)
# for edge in range(number_of_edges):
#     clear()
#     g.addEdge(int(input("Enter from edge: ")), int(
#         input("Enter to edge: ")), int(input("Enter edge weight: ")))

g = Graph(4)
g.addEdge(0, 1, 4)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()
