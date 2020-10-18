from particula import Particula

class Laboratorio:
    
    def __init__(self):
        self.__particulas = []

    def __str__(self):
        return "".join(
            str(p) + '\n' for p in self.__particulas
        )

    def agregar_final(self, p: Particula):
        self.__particulas.append(p)

    def agregar_inicio(self, p: Particula):
        self.__particulas.insert(0, p)

    def mostrar(self):
        for p in self.__particulas:
            print(p)