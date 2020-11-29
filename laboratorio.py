from particula import Particula
from collections import deque
import pprint
import json

class Laboratorio:
    
    def __init__(self):
        self.__particulas = []
        self.__grafo = dict()

    def __str__(self):
        return "".join(
            str(p) + '\n' for p in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            p = self.__particulas[self.cont]
            self.cont += 1
            return p
        else:
            raise StopIteration

    def agregar_inicio(self, p: Particula):
        self.__particulas.insert(0, p)

    def agregar_final(self, p: Particula):
        self.__particulas.append(p)

    def ordenar_id(self):
        self.__particulas.sort(key=lambda p: p.getID)

    def ordenar_distancia(self):
        self.__particulas.sort(key=lambda p: p.getDistancia, reverse=True)

    def ordenar_velocidad(self):
        self.__particulas.sort(key=lambda p: p.getVelocidad)

    def mostrar(self):
        for p in self.__particulas:
            print(p)

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [p.to_dict() for p in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**p) for p in lista]
            return 1
        except:
            return 0

    def establecer_grafo(self):
        self.__grafo.clear()
        for p in self.__particulas:
            origen = (p.getOrigenX, p.getOrigenY)
            destino = (p.getDestinoX, p.getDestinoY)
            peso = int(p.getDistancia)
            arista_o_d = (destino, peso)
            arista_d_o = (origen, peso)
            if origen in self.__grafo:
                self.__grafo[origen].append(arista_o_d)
            else:
                self.__grafo[origen] = [arista_o_d]
            if destino in self.__grafo:
                self.__grafo[destino].append(arista_d_o)
            else:
                self.__grafo[destino] = [arista_d_o]
        return pprint.pformat(self.__grafo, width=100, indent=1)

    def busqueda_profundidad(self, origen: tuple):
        self.visitados = []
        self.recorrido = []
        self.pila = deque()
        self.visitados.append(origen)
        self.pila.append(origen)
        while self.pila:
            vertice = self.pila.pop()
            self.recorrido.append(vertice)
            for key, value in self.__grafo[vertice]:
                if key not in self.visitados:
                    self.visitados.append(key)
                    self.pila.append(key)
        return "".join(str(t) + '\n' for t in self.recorrido)

    def busqueda_amplitud(self, origen: tuple):
        self.visitados = []
        self.recorrido = []
        self.cola = deque()
        self.visitados.append(origen)
        self.cola.append(origen)
        while self.cola:
            vertice = self.cola.popleft()
            self.recorrido.append(vertice)
            for key, value in self.__grafo[vertice]:
                if key not in self.visitados:
                    self.visitados.append(key)
                    self.cola.append(key)
        return "".join(str(t) + '\n' for t in self.recorrido)
