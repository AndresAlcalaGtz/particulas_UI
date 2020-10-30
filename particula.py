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
            "Origen (x,y): (" + str(self.__origenX) + ", " + str(self.__origenY) + ")\n" +
            "Destino (x,y): (" + str(self.__destinoX) + ", " + str(self.__destinoY) + ")\n" +
            "Velocidad: " + str(self.__velocidad) + "\n" +
            "RGB: (" + str(self.__red) + ", " + str(self.__green) + ", " + str(self.__blue) + ")\n" +
            "Distancia: " + str(self.__distancia) + "\n"
        )

    @property
    def getID(self):
        return self.__id

    @property
    def getOrigenX(self):
        return self.__origenX

    @property
    def getOrigenY(self):
        return self.__origenY

    @property
    def getDestinoX(self):
        return self.__destinoX

    @property
    def getDestinoY(self):
        return self.__destinoY

    @property
    def getVelocidad(self):
        return self.__velocidad

    @property
    def getRed(self):
        return self.__red

    @property
    def getGreen(self):
        return self.__green

    @property
    def getBlue(self):
        return self.__blue

    @property
    def getDistancia(self):
        return self.__distancia

    def to_dict(self):
        return {
            "ID": self.__id,
            "OrigenX": self.__origenX,
            "OrigenY": self.__origenY,
            "DestinoX": self.__destinoX,
            "DestinoY": self.__destinoY,
            "Velocidad": self.__velocidad,
            "Red": self.__red,
            "Green": self.__green,
            "Blue": self.__blue
        }