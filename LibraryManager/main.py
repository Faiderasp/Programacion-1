from src.services.AppConsole import AppConsole
from src.services.Biblioteca import Biblioteca
if __name__ == "__main__":
    biblioteca = Biblioteca()
    app = AppConsole(biblioteca)

    app.correr_aplicacion()