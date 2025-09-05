from datetime import datetime as dt
from ..models.MaterialBiblioteca import MaterialBiblioteca

class Prestamo:
    def __init__(self,
                 materialBiblioteca:MaterialBiblioteca,
                 fechaPrestamo:dt = None,
                 usuarioN:str = None,
                 fechaDevolucion:dt = None):
        self.__materialBiblioteca = MaterialBiblioteca
        self.__fechaPrestamo = fechaPrestamo
        self.__fechaDevolucion = fechaDevolucion
        self.__usuario = usuarioN

    def getMaterialBiblioteca(self)->MaterialBiblioteca:
        return self.__materialBiblioteca
    def setMaterialBiblioteca(self,nuevoMaterialBiblioteca):
        self.__materialBiblioteca = nuevoMaterialBiblioteca

    def getfechaPrestamo(self)->dt:
        return self.__fechaPrestamo
    def setfechaPrestamo(self,nuevaFechaPrestamo: dt):
        self.__fechaPrestamo = nuevaFechaPrestamo

    def getfechaDevolucion(self)->dt:
        return self.__fechaDevolucion
    def setfechaDevolucion(self,nuevaFechaDevolucion: dt):
        self.__fechaDevolucion = nuevaFechaDevolucion

    def getNombreUsuario(self)->str:
        return self.__usuario
    def setNombreUsuario(self,nuevoNombre):
        self.__usuario = nuevoNombre
    
        