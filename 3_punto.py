import heapq  # importamos la biblioteca heapq para utilizar una cola de prioridad


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_vertice(self, v):
        """
        Agrega un nuevo vértice al grafo.
        
        Args:
            v (str): el nombre del nuevo vértice que se va a agregar.
        """
        self.vertices[v] = []

    def agregar_arista(self, u, v, peso):
        """
        Agrega una nueva arista al grafo.
        
        Args:
            u (str): el nombre del vértice origen de la arista.
            v (str): el nombre del vértice destino de la arista.
            peso (float): el peso o costo de la arista.
        """
        if u not in self.vertices:
            self.agregar_vertice(u)
        if v not in self.vertices:
            self.agregar_vertice(v)
        self.aristas[(u, v)] = peso
        self.vertices[u].append(v)

    def eliminar_vertice(self, v):
        """
        Elimina un vértice y todas sus aristas del grafo.
        
        Args:
            v (str): el nombre del vértice que se va a eliminar.
        """
        if v in self.vertices:
            # Eliminar aristas que conectan al vértice
            for u, vecinos in self.vertices.items():
                if v in vecinos:
                    self.aristas.pop((u, v), None)
                    self.vertices[u] = [vecino for vecino in vecinos if vecino != v]
            
            # Eliminar el vértice
            self.vertices.pop(v, None)
    def camino_minimo(self, inicio, fin):
        """
        Encuentra el camino mínimo y la distancia mínima desde un vértice de inicio hasta un vértice de fin,
        utilizando el algoritmo de Dijkstra.

        Args:
            inicio (str): El vértice de inicio del camino.
            fin (str): El vértice de fin del camino.

        Returns:
            tuple: Una tupla con dos elementos:
                - Una lista de vértices que representan el camino mínimo desde inicio hasta fin.
                - La distancia mínima desde inicio hasta fin.
                  Si no hay camino posible, retorna None para ambos elementos.
        """
        if inicio not in self.vertices or fin not in self.vertices:
            return None, None

        # Aplicar Dijkstra para encontrar las distancias mínimas a cada nodo
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0
        heap = [(0, inicio)]
        visitados = set()
        padre = {}

        while heap:
            (dist, actual) = heapq.heappop(heap)
            if actual in visitados:
                continue
            visitados.add(actual)

            for vecino in self.vertices[actual]:
                peso = self.aristas[(actual, vecino)]
                distancia_alternativa = dist + peso
                if distancia_alternativa < distancias[vecino]:
                    distancias[vecino] = distancia_alternativa
                    padre[vecino] = actual
                    heapq.heappush(heap, (distancia_alternativa, vecino))

        # Construir camino mínimo
        if distancias[fin] == float('inf'):
            return None, None

        camino = [fin]
        while camino[-1] != inicio:
            camino.append(padre[camino[-1]])
        camino.reverse()

        return camino, distancias[fin]
    
    def es_fuertemente_conexo(self):
        """
        Verifica si el grafo es fuertemente conexo utilizando DFS en ambas direcciones desde un nodo inicial.
        
        Returns:
            bool: True si el grafo es fuertemente conexo, False en caso contrario.
        """
        if not self.vertices:
            return False

        # Realizar DFS en ambos sentidos desde el primer nodo del grafo
        primer_nodo = next(iter(self.vertices))
        visitados_ida = set()
        self._dfs_ida(primer_nodo, visitados_ida)
        if len(visitados_ida) != len(self.vertices):
            return False

        visitados_vuelta = set()
        self._dfs_vuelta(primer_nodo, visitados_vuelta)
        if len(visitados_vuelta) != len(self.vertices):
            return False

        return True

    def _dfs_ida(self, actual, visitados):
        """
        Realiza DFS en sentido ida desde el nodo actual y agrega los nodos visitados al conjunto "visitados".
        """
        visitados.add(actual)
        for vecino in self.vertices[actual]:
            if vecino not in visitados:
                self._dfs_ida(vecino, visitados)

    def _dfs_vuelta(self, actual, visitados):
        """
        Realiza DFS en sentido vuelta desde el nodo actual y agrega los nodos visitados al conjunto "visitados".
        """
        visitados.add(actual)
        for u, v in self.aristas:
            if v == actual and u not in visitados:
                self._dfs_vuelta(u, visitados)

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_vertice('8')
grafo.agregar_vertice('0')
grafo.agregar_vertice('7')
grafo.agregar_vertice('6')
grafo.agregar_vertice('3')
grafo.agregar_vertice('9')
grafo.agregar_vertice('4')
grafo.agregar_vertice('2')
grafo.agregar_vertice('5')
grafo.agregar_vertice('1')

# Agregar aristas con costos
grafo.agregar_arista('8', '0', 464)
grafo.agregar_arista('0', '5', 343)
grafo.agregar_arista('2', '5', 1054)
grafo.agregar_arista('4', '2', 1364)
grafo.agregar_arista('4', '5', 1106)
grafo.agregar_arista('0', '7', 1435)
grafo.agregar_arista('5', '1', 879)
grafo.agregar_arista('9', '4', 766)
grafo.agregar_arista('1', '9', 524)
grafo.agregar_arista('7', '1', 811)
grafo.agregar_arista('7', '6', 837)
grafo.agregar_arista('1', '6', 954)
grafo.agregar_arista('6', '3', 433)
grafo.agregar_arista('3', '9', 1053)

print(grafo.es_fuertemente_conexo())  # False
validacion = grafo.es_fuertemente_conexo()

if validacion == False:
    print("El grafo no es fuertemente conexo")
else:
    print("El grafo es fuertemente conexo")



