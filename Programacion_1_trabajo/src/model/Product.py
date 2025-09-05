from abc import ABC
from ..view.View import View

class Product(ABC):

    def __init__(self, name:str, price:float, seller:str, color:str):
        self.name = name
        self.price = price
        self.seller = seller
        self.color = color
    
    def setProduct(self, *args):
        for arg in args:
            match arg:
                case "name":
                    self.name = View.askString("Insert the new name")
                case "price":
                    self.price = View.askFloat("Insert a new price")
                case "color":
                    self.color = View.askFloat("Insert the new color")
                case _:
                    View.printError("Please insert a valid input")
        