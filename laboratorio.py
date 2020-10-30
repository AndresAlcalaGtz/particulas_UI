from particula import Particula
import json

class Laboratorio:
    
    def __init__(self):
        self.__particulas = []

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

    def agregar_final(self, p: Particula):
        self.__particulas.append(p)

    def agregar_inicio(self, p: Particula):
        self.__particulas.insert(0, p)

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