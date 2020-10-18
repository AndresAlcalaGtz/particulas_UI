from algoritmos import distancia_euclidiana

class Particula:

    def __init__(self, ID=0, OrigenX=0, OrigenY=0, DestinoX=0, DestinoY=0, Velocidad=0, Red=0, Green=0, Blue=0):
        self.__id = ID
        self.__origenX = OrigenX
        self.__origenY = OrigenY
        self.__destinoX = DestinoX
        self.__destinoY = DestinoY
        self.__velocidad = Velocidad
        self.__red = Red
        self.__green = Green
        self.__blue = Blue
        self.__distancia = distancia_euclidiana(OrigenX, OrigenY, DestinoX, DestinoY)

    def __str__(self) -> str:
        return (
            "ID: " + str(self.__id) + "\n" +
            "Origen x: " + str(self.__origenX) + "\n" +
            "Origen y: " + str(self.__origenY) + "\n" +
            "Destino x: " + str(self.__destinoX) + "\n" +
            "Destino y: " + str(self.__destinoY) + "\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "RGB: (" + str(self.__red) + ", " + str(self.__green) + ", " + str(self.__blue) + ")\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )