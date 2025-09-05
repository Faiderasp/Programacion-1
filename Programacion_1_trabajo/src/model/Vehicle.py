from ..model.Product import Product
from ..view.View import View

class Vehicle(Product):
    def __init__(self, name:str, price:float, seller:str, color:str, model:str, cc:float):
        super().__init__(name, price, seller, color)
        self.model = model
        self.cc = cc

    def setProduct(self, *args):
        for arg in args:
            match arg:
                case "name":
                    self.name = View.askString("Insert the new name")
                case "price":
                    self.price = View.askFloat("Insert the new price")
                case "color":
                    self.color = View.askString("Insert the new color")
                case "model":
                    self.model = View.askString("Insert the new model")
                case "cpu":
                    self.cc = View.askFloat("Insert the new cc")
                case _:
                    View.printError("Please insert a valid input")