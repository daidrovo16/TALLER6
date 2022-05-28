# Importacion de librerias
from collections import defaultdict
from numpy import var

#Implementacion de la clase grafo
#haciendo uso de las listas de adyacencia
class Grafos:
    
    # Constructor
    def __init__(self):
        #Se realiza la implementacion de un diccionario de datos
        #para el almacenamiento de los nodos del grafo
        self.Grafos = defaultdict(list)
    #Se implementa la funcion de agregacion de un borde al grafo
    def agrega_Borde(self, u, v):
        self.Grafos[u].append(v)
        
    # Funcion para el uso de Busqueda en profundidad(DFS)sfdsfdsfs
    def busqueda_Prufunda(self, v, busqueda_Marcada):
        
        #Funcion que visita o marca el nodo y lo muestra como obtenido
        busqueda_Marcada.add(v)
        print(v, end=' ')
    
        # Funcion que indica la recurrencia de los vertices adyacentes
        # al vertice obtenido
        for visita_Vertice in self.Grafos[v]:
            if visita_Vertice not in busqueda_Marcada:
                self.busqueda_Prufunda(visita_Vertice, busqueda_Marcada)

    # Funcion para hacer el recorrido en DFS. Uso de recursividad 
    # en la busqueda por profundidad
    def busqueda(self, v):
        
        #Crea una lista, la cual almacena los nodos visitados
        busqueda_Marcada = set()
        
        # Se genera un llamada a la funcion recursiva,
        # la cual muestra el recorrido del arbol
        
        self.busqueda_Prufunda(v, busqueda_Marcada) 

# Se crea un grafo predeterminado por datos definido
g = Grafos()
g.agrega_Borde(0, 1)
g.agrega_Borde(0, 2)
g.agrega_Borde(1, 2)
g.agrega_Borde(2, 0)
g.agrega_Borde(2, 3)
g.agrega_Borde(3, 3)
 
print("Se muestra un recorrido por busqueda en Profundidadss")
g.busqueda(2)
