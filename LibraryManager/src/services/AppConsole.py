from ..services.Biblioteca import Biblioteca
from ..models.Usuario import Usuario
from ..models.Prestamos import Prestamo
from datetime import datetime

class AppConsole:
    def __init__(self, biblioteca: Biblioteca):
        self.__biblioteca = biblioteca

    def menu_principal(self) -> int:
        print("""
===== SISTEMA DE GESTION BIBLIOTECARIO =====
1.  Crear Usuario
2.  Prestar Material
3.  Devolver Material
0.  Salir
              """)
        return int(input("Ingrese la opcion deseada: "))

    def correr_aplicacion(self):
        self.__biblioteca.precargar_informacion()
        aplicacion_activa = True
        user = None
        while aplicacion_activa:
            self.__biblioteca.mostrar_material()
            match self.menu_principal():
                case 1:
                    user = Usuario(input("Ingrese el nombre del usuario: "), input("Ingrese la identificacion del usuario: "))
                    self.__biblioteca.añadir_usuario(user)
                case 2:
                    nombreMaterial = input("Ingrese el nombre del material: ")
                    material = self.__biblioteca.buscar_material(nombreMaterial)
                    if material is not None:
                        idUsuario = input("Ingrese la identificacion del usuario: ")
                        usuario = self.__biblioteca.buscar_usuario(idUsuario)
                        if usuario is not None:
                                self.__biblioteca.añadir_prestamo(Prestamo(materialBiblioteca = material,
                                                                           fechaPrestamo= datetime.now(),
                                                                           fechaDevolucion = material.calcular_fecha_devolucion(datetime.now()),
                                                                           usuarioN = usuario))
                                user.añadirElemento(material.getNombre())
                                print(f"Los prestamos activos de {user.getNombre()} son {user.getLibros()}")
                        else:
                            print("El usuario no coincide. ")
                    else:
                        print("El material no coincide. ")
                case 3:
                    material = input("Que material deseas devolver? : ")
                    if self.__biblioteca.buscar_material(material):
                        self.__biblioteca.devolver_material(material)
                        user.eliminarElemento(material)
                        print(f"Los prestamos activos de {user.getNombre()} son {user.getLibros()}")

                case 0:
                    print("Saliendo de la aplicacion...")
                    aplicacion_activa = False
                case _:
                    print("Por favor ingrese una opcion valida. ")
                    
