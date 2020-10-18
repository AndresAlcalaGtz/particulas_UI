import math

def distancia_euclidiana(x_1: int, y_1: int, x_2: int, y_2: int) -> float:
    return math.sqrt((math.pow(x_2 - x_1, 2)) + (math.pow(y_2 - y_1, 2)))