from ..models.MaterialBiblioteca import MaterialBiblioteca
from datetime import datetime, timedelta

class Audiovisual(MaterialBiblioteca):
    
    def __init__(self,nombre:str,anio:int,autor:str,genero:str):
        super().__init__(
            nombre=nombre,
            anio=anio,
            autor=autor)
        self.__genero = genero

    def getGenero(self)->str:
        return self.__genero

    def setGenero(self,nuevagenero):
        self.__genero = nuevagenero
    
    def obtener_tipo(self):
        return "Audiovisual"

    def obtener_detalles(self):
        return super().obtener_detalles() + (f" - Genero : {self.__genero}")

    def calcular_fecha_devolucion(self, date):
        return date + timedelta(days = 3)