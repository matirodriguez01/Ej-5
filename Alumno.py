class Alumno:

    faltperm: int = 30
    nclases = 300

    def __init__(self, nom, a, div, falt=0):
        self.__nombre = nom
        self.__anio = a
        self.__division = div
        self.__faltas = falt

    def getporcentaje (self):
        porc = int(self.faltperm) * 100 / int(self.__faltas)
        return porc

    def getnombre (self):
        return self.__nombre

    def getanio (self):
        return self.__anio

    def getdiv (self):
        return self.__division

    def getfaltas (self):
        return self.__faltas

    @classmethod
    def cambiarpermitidas(cls, cant):
        cls.permitidas = cant
        print('Nueva cantidad de asistencias permitidas: ', cls.permitidas)
