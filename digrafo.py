class Grafo:
    def __init__(self):
        self.nodos = {}  # Diccionario que guarda los nodos del grafo
        self.arcos = []  # Lista que guarda los arcos del grafo

    @staticmethod
    def crearGrafo(letraNodo):
        grafo = Grafo()
        for letra in letraNodo:
            grafo.nodos[letra] = []
        return grafo

    def insertarNodo(self, nodo):
        self.nodos[nodo] = []
        self.arcos = [(nodo1, nodo2) for nodo1, nodo2 in self.arcos if nodo1 != nodo and nodo2 != nodo]

    def insertarArco(self, nodo1, nodo2):
        self.arcos.append((nodo1, nodo2))
        self.nodos[nodo1].append(nodo2)

    def eliminarNodo(self, nodo):
        # Eliminar arcos que involucran al nodo
        self.arcos = [(nodo1, nodo2) for nodo1, nodo2 in self.arcos if nodo1 != nodo and nodo2 != nodo]
        # Eliminar el nodo de la estructura de datos del grafo
        del self.nodos[nodo]
        # Ajustar la lista de adyacencia de los nodos restantes
        for nodo2 in self.nodos:
            if nodo in self.nodos[nodo2]:
                self.nodos[nodo2].remove(nodo)

    def eliminarArco(self, nodo1, nodo2):
        if (nodo1, nodo2) in self.arcos:
            self.arcos.remove((nodo1, nodo2))
            self.nodos[nodo1].remove(nodo2)

    def adyacente(self, nodo1, nodo2):
        return nodo2 in self.nodos[nodo1]

    def grado(self, nodo):
        return len(self.nodos[nodo])

    def recorrido(self, nodo, visitados=None):
        if visitados is None:
            visitados = []
        visitados.append(nodo)
        for nodo2 in self.nodos[nodo]:
            if nodo2 not in visitados:
                self.recorrido(nodo2, visitados)
        return visitados

    def obtenerArcos(self):
        return self.arcos


# Creamos nuestro grafo
g = Grafo()

# Agregamos algunos nodos
g.insertarNodo('A')
g.insertarNodo('B')
g.insertarNodo('C')
g.insertarNodo('D')

# Agregamos algunos arcos
g.insertarArco('A', 'B')
g.insertarArco('B', 'C')
g.insertarArco('C', 'D')
g.insertarArco('D', 'A')

# Eliminamos algunos nodos y arcos
g.eliminarNodo('C')
g.eliminarArco('D', 'A')

# Imprimimos el grafo resultante
print("Nodos: ", g.nodos)

print("Arcos: ", g.arcos)

# Realizamos algunas operaciones en el grafo
print("¿B es adyacente a A? ", g.adyacente('A', 'B'))
print("¿A es adyacente a B? ", g.adyacente('B', 'A'))
print("Grado del nodo A: ", g.grado('A'))
print("Recorrido del nodo B: ", g.recorrido('B'))

# Obtener el conjunto de nodos
V = g.nodos.keys()

# Obtener la lista de arcos
A = g.obtenerArcos()

# Crear el par D=(V,A)
D = (V,A)

# Imprimir el resultado
print("D = ", D)