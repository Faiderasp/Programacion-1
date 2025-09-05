class Usuario:
    def __init__(self,nombre:str,ident:int,elementos:list[str]=[]):
        self.__nombre = nombre
        self.__id = ident
        self.__elementos = elementos

    def getNombre(self)->str:
        return self.__nombre
    
    def setNombre(self,nombrenuevo):
        self.__nombre = nombrenuevo

    def getId(self)->int:
        return self.__id
    
    def setId(self,IdNuevo):
        self.__id = IdNuevo

    def getLibros(self)->list:
        return self.__elementos
    
    def setNombre(self,libros:list):
        self.__elementos = libros

    def añadirElemento(self,elemento:str):
        self.__elementos.append(elemento)

    def eliminarElemento(self, elemento:str):
        self.__elementos.remove(elemento)
    
    