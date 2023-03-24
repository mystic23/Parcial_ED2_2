"""
El siguiente codigo lo saque de aquí:
https://www.techiedelight.com/es/check-graph-strongly-connected-one-dfs-traversal/


"""

class Graph:
	def __init__(self, edges, n):

            """
            Constructor de la clase Graph.

            Parameters:
            -----------
            edges: list
                Una lista de tuplas que representan las aristas del grafo.
            n: int
                El número total de nodos en el grafo.
             """
            self.adjList = [[] for _ in range(n)]
            for (src, dest) in edges:
                self.adjList[src].append(dest)

def DFS(graph, v, discovered, arrival, isSC, time):
    # """   
    # Realiza un recorrido en profundidad para determinar si el grafo es fuertemente conexo.


    # Args:
    #     graph :  Objeto que representa el grafo.
    #     v : Nodo en el que se comienza el recorrido.
    #     discovered :  Arreglo para mantener un registro de los nodos visitados.
    #     arrival : Arreglo para mantener un registro de los tiempos de llegada a cada nodo.
    #     isSC :Variable para determinar si el grafo es fuertemente conexo.
    #     time : Variable para mantener un registro del tiempo transcurrido durante el recorrido.
    # return:
    # arr:  El tiempo de llegada más temprano en el grafo.
    # isSC:Variable que indica si el grafo es fuertemente conexo.
    # time: Variable que mantiene un registro del tiempo transcurrido durante el recorrido.
    
    # """
	if not isSC:
		return 0, isSC, time
	time = time + 1
	arrival[v] = time
	discovered[v] = True
	arr = arrival[v]
	for w in graph.adjList[v]:

		if not discovered[w]:
			_arr, isSC, time = DFS(graph, w, discovered, arrival, isSC, time)
			arr = min(arr, _arr)
		else:
			arr = min(arr, arrival[w])
	if v and arr == arrival[v]:
		isSC = False
	return arr, isSC, time
def isStronglyConnected(graph, n):
    # """
    # Determina si un grafo es fuertemente conexo.

    # Args:
    # graph (list): Lista de adyacencia que representa el grafo.
    # n (int): Número de vértices del grafo.
    # """
	discovered = [False] * n
	arrival = [0] * n
	isSC = True
	time = -1
	isSC = DFS(graph, 0, discovered, arrival, isSC, time)[1]
	for i in range(n):
		if not discovered[i]:
			isSC = False
	return isSC
if __name__ == '__main__':

	edges = [(8,0), (0,5), (2,5), (4,2), (4,5), (0,7), (5,1), (9,4), (1,9), (7,1), (7,6), (1,6), (6,3), (3,9)]
	n = 10
	graph = Graph(edges, n)

	if isStronglyConnected(graph, n):
		print('The graph is strongly connected')
	else:
		print('The graph is not strongly connected')