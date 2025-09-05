from ..models.MaterialBiblioteca import MaterialBiblioteca
from ..models.Libro import Libro
from ..models.Revista import Revista
from ..models.Audiovisual import Audiovisual
from ..models.Usuario import Usuario
from ..models.Prestamos import Prestamo

from datetime import datetime as dt
class Biblioteca():

    def __init__(self, usuarios: list[Usuario] = [], materialBiblioteca: list[MaterialBiblioteca] = [],prestamos:list[Prestamo] = []):
        self.__usuarios = usuarios
        self.__materialBiblioteca = materialBiblioteca
        self.__prestamos = prestamos
        
    def getUsuarios(self)->list[Usuario]:
        return self.__usuarios
    
    def getMaterialBiblioteca(self)->list[MaterialBiblioteca]:
        return self.__materialBiblioteca
    
    def getPrestamos(self)->list[Prestamo]:
        return self.__prestamos
    
    def setUsuarios(self, usuarios):
        self.__usuarios = usuarios

    def setMaterialBiblioteca(self, materialBiblioteca):
        self.__materialBiblioteca = materialBiblioteca

    def añadir_usuario(self, usuario):
        self.__usuarios.append(usuario)
        
    def buscar_material(self, nombre):
        for material in self.__materialBiblioteca:
            if nombre == material.getNombre():
                return material
        return None

    def buscar_usuario(self, id):
        for usuario in self.__usuarios:
            if id == usuario.getId():
                return usuario
        return None

    def añadir_prestamo(self, prestamo):
        self.__prestamos.append(prestamo)
    
    def devolver_material(self, material:str):
        for prestamo in self.__prestamos:
            if material == prestamo.getMaterialBiblioteca():
                prestamo.setfechaDevolucion(dt.now())

    def precargar_informacion(self):
        libros = [("Don Quijote de La Mancha" , 1605, "Miguel de Cervantes", "Lenguaje", "978-9977-58-319-8"), 
                  ("Cien Anios de Soledad", 1967, "Gabriel Garcia Marquez", "Lenguaje", "978-8437604947")]
        revistas = [("Glamour Chic", 2028, "Carpet Moments", "Fashion Forward"), 
                    ("Histroia", 2018, "Mary Beard", "National Geographic")]
        audiovisuales = [("Despacito", 2017, "Luis Fonsi", "Musica"),
                          ("PPC", 2025, "Roa", "Musica")]
        
        for libro in libros:
            self.__materialBiblioteca.append(Libro(nombre=libro[0], 
                                                   anio=libro[1],
                                                   autor=libro[2],
                                                   materia=libro[3],
                                                   isbn=libro[4]))
            
        for revista in revistas:
            self.__materialBiblioteca.append(Revista(nombre=revista[0], 
                                                   anio=revista[1],
                                                   autor=revista[2],
                                                   marca=revista[3]))
            
        for audiovisual in audiovisuales:
            self.__materialBiblioteca.append(Audiovisual(nombre=audiovisual[0], 
                                                   anio=audiovisual[1],
                                                   autor=audiovisual[2],
                                                   genero=audiovisual[3]))

    def mostrar_material(self):
        print("===== MATERIAL BIBLIOTECA ======")
        for material in self.__materialBiblioteca:
            print(f"{material.obtener_tipo()} - Nombre : {material.getNombre()} - Autor : {material.getAutor()}")




    
