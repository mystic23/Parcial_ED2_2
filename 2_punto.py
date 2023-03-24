class Grafo:
    def __init__(self):
        """
        Inicializa el grafo vacío

        """
        self.vertices = set()
        self.aristas = []

    def agregar_vertice(self, vertice):
        """
        Agrega un nuevo vértice al grafo

        Args:
            vertice: El nuevo vértice a agregar

 
        """
        self.vertices.add(vertice)

    def agregar_arista(self, inicio, fin, costo):
        """
        Agrega una nueva arista al grafo.

        Args:
            inicio: El vértice de inicio de la arista.
            fin: El vértice final de la arista.
            costo: El costo de la arista.

        """
        self.aristas.append((inicio, fin, costo))

    def buscar_padre(self, padres, vertice):
        """
        Busca el padre del vertice dado en el diccionario de padres.

        Args:
            padres: El diccionario de padres.
            vertice: El vértice cuyo padre se quiere buscar.

        """
        if padres[vertice] == vertice:
            return vertice
        return self.buscar_padre(padres, padres[vertice])

    def unir(self, padres, rango, vertice1, vertice2):
        """
        Une los subárboles de los vértices dados en un solo árbol.

        Args:
            padres: El diccionario de padres.
            rango: El diccionario de rangos.
            vertice1: El primer vértice a unir.
            vertice2: El segundo vértice a unir.

      
        """
        padre1 = self.buscar_padre(padres, vertice1)
        padre2 = self.buscar_padre(padres, vertice2)

        if rango[padre1] > rango[padre2]:
            padres[padre2] = padre1
        elif rango[padre1] < rango[padre2]:
            padres[padre1] = padre2
        else:
            padres[padre2] = padre1
            rango[padre1] += 1

    def kruskal(self):
        """
        Aplica el algoritmo de Kruskal para encontrar el árbol de expansión mínima del grafo.

        Returns:
            Grafo: Un nuevo grafo con las aristas del árbol de expansión mínima.
        """
        self.aristas.sort(key=lambda x: x[2])
        aristas_arbol = []
        padres = {}
        rango = {}
        for vertice in self.vertices:
            padres[vertice] = vertice
            rango[vertice] = 0
        for arista in self.aristas:
            inicio, fin, costo = arista
            if self.buscar_padre(padres, inicio) != self.buscar_padre(padres, fin):
                self.unir(padres, rango, inicio, fin)
                aristas_arbol.append(arista)
        grafo_arbol = Grafo()
        for vertice in self.vertices:
            grafo_arbol.agregar_vertice(vertice)
        for arista in aristas_arbol:
            inicio, fin, costo = arista
            grafo_arbol.agregar_arista(inicio, fin, costo)

        return grafo_arbol
    
    def dfs(self, vertice, visitados):
        """
            implementa una búsqueda en profundidad (DFS) recursiva a partir de un vértice dado en un grafo.

            Args:
            vertice (any): El vértice desde el cual se iniciará la búsqueda.
            visitados (set): Conjunto de vértices visitados en la búsqueda.
        """
        visitados.add(vertice)
        for arista in self.aristas:
            if vertice in arista[:2]:
                vecino = arista[0] if arista[1] == vertice else arista[1]
                if vecino not in visitados:
                    self.dfs(vecino, visitados)

    def es_conexo(self):
        """ 
        determina si un grafo es conexo (es decir, si hay un camino entre cualquier par de vértices)
            mediante la ejecución de una búsqueda en profundidad desde el primer vértice en la lista de vértices.
        """
        visitados = set()
        self.dfs(list(self.vertices)[0], visitados)
        return len(visitados) == len(self.vertices)

print("\n")
print("Forma de esclavos D: )")
print("---------------------")
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


grafo.agregar_arista('8', '0', 464)
grafo.agregar_arista('0', '5', 343)
grafo.agregar_arista('5', '2', 1054)
grafo.agregar_arista('2', '4', 1364)
grafo.agregar_arista('4', '5', 1106)
grafo.agregar_arista('0', '7', 1435)
grafo.agregar_arista('5', '1', 879)
grafo.agregar_arista('4', '9', 766)
grafo.agregar_arista('1', '9', 524)
grafo.agregar_arista('7', '1', 811)
grafo.agregar_arista('7', '6', 837)
grafo.agregar_arista('1', '6', 954)
grafo.agregar_arista('6', '3', 433)
grafo.agregar_arista('9', '3', 1053)


arbol_expansion = grafo.kruskal()
for inicio, fin, costo in arbol_expansion.aristas:
    print(inicio, "---", fin, "peso:", costo)
    
costos = []
for arista in arbol_expansion.aristas:
    # Extraer el tercer valor de la tupla (el costo de la arista)
    costo = arista[2]
    # Agregar el costo a la lista de costos
    costos.append(costo)
# Sumar todos los costos para obtener el costo total
costo_total = sum(costos)
print("Costo total del árbol de expansión mínima:", costo_total)


