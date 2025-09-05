from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class MaterialBiblioteca(ABC):
    
    def __init__(self, nombre: str, autor: str, anio: int):
        self.__nombre = nombre
        self.__autor = autor
        self.__anio = anio

    def getIsbn(self):
        return self.__isbn

    def getNombre(self):
        return self.__nombre
    
    def getAutor(self):
        return self.__autor
    
    def getAnio(self):
        return self.__anio
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setAutor(self, autor):
        self.__autor = autor

    def setAnio(self, isbn):
        self.__isbn = isbn

    @abstractmethod
    def calcular_fecha_devolucion(self) -> datetime:
        pass
    
    @abstractmethod
    def obtener_tipo(self) -> str:
        pass
    
    def obtener_detalles(self) -> str:
        return (f"Nombre : {self.__nombre} - Autor : {self.__autor} - Anio : {self.__anio}")

    
