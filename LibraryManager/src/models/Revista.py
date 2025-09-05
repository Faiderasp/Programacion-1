from .MaterialBiblioteca import MaterialBiblioteca
from datetime import datetime, timedelta

class Revista(MaterialBiblioteca):
    
    def __init__(self,nombre:str,anio:int,autor:str,marca:str):
        super().__init__(
            nombre=nombre,
            anio=anio,
            autor=autor)
        self.__marca = marca
    
    def getMarca(self)->str:
        return self.__marca
    def setMarca(self,nuevamarca):
        self.__marca = nuevamarca

    def obtener_tipo(self):
        return "Revista"

    def obtener_detalles(self):
        return super().obtener_detalles() + (f" - Marca : {self.__marca}")
    
    def calcular_fecha_devolucion(self, date):
        return date + timedelta(days = 7)