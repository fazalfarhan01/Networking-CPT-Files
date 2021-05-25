from terminaltables import SingleTable
from common import clear
class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = []

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])
		
	# utility function used to print the solution
	def printArr(self,src, dist):
		clear()
		sourceInfo = ["Source"], [src]
		sourceTable = SingleTable(sourceInfo)
		print(sourceTable.table)

		data = ["Vertex"]+list(range(self.V)), ["Distance from source"]+dist
		table = SingleTable(data)
		print(table.table)
	
	def BellmanFord(self, src):
		dist = [float("Inf")] * self.V
		dist[src] = 0
		for _ in range(self.V - 1):
			for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						dist[v] = dist[u] + w
		for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						print("Graph contains negative weight cycle")
						return
		self.printArr(src,dist)

# g = Graph(5)
# g.addEdge(0, 1, -1)
# g.addEdge(0, 2, 4)
# g.addEdge(1, 2, 3)
# g.addEdge(1, 3, 2)
# g.addEdge(1, 4, 2)
# g.addEdge(3, 2, 5)
# g.addEdge(3, 1, 1)
# g.addEdge(4, 3, -3)

g = Graph(4)
g.addEdge(0,1,4)
g.addEdge(0,3,5)
g.addEdge(1,3,4)
g.addEdge(3,2,3)
g.addEdge(2,1,-5)

g.BellmanFord(0)