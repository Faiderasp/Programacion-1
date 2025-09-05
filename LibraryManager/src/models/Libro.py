from .MaterialBiblioteca import MaterialBiblioteca
from datetime import datetime, timedelta
class Libro(MaterialBiblioteca):
    
    def __init__(self,nombre:str,anio:int,isbn:str,autor:str,materia:str):
        super().__init__(
            nombre=nombre,
            anio=anio,
            autor=autor)
        self.__materia = materia
        self.__isbn = isbn

    def getMateria(self)->str:
        return self.__materia

    def setMateria(self,nuevamateria):
        self.__materia = nuevamateria

    def getIsbn(self):
        return self.__isbn
    
    def setIsbn(self, isbn):
        self.__isbn = isbn

    def obtener_tipo(self):
        return "Libro"

    def obtener_detalles(self):
        return super().obtener_detalles() + (f" - Materia : {self.__materia} - ISBN : {self.__isbn}")

    def calcular_fecha_devolucion(self, date):
        return date + timedelta(days = 15)
        

