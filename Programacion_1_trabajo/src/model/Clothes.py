from ..model.Product import Product
from ..view.View import View

class Clothes(Product):
    def __init__(self, name:str, price:float, seller:str, color:str, cloth:str):
        super().__init__(name, price, seller, color)
        self.cloth = cloth

    def setProduct(self, *args):
        for arg in args:
            match arg:
                case "name":
                    self.name = View.askString("Insert the new name")
                case "price":
                    self.price = View.askFloat("Insert the new price")
                case "color":
                    self.color = View.askString("Insert a new color")
                case "cloth":
                    self.cloth = View.askString("Insert the new cloth")
                case _:
                    View.printError("Please insert a valid input")

        