from ..model.Product import Product
class User():

    def __init__(self, name: str, email: str, password: str, seller: bool = False,product: list = []):
        self.name = name
        self.__email = email
        self.__password = password
        self.seller = seller
        self.__product = product

    def BuyProduct(self,product: dict)->None:
        print(product)
        self.__product.append(product['name'])

    def getPassword(self):
        return self.__password
    
    def setPassword(self,newPass:str,oldPass:str):
        if oldPass == self.__password:
            self.__password == newPass
        else:
            return
        
    def getEmail(self):
        return self.__email

    def getProduct(self):
        return self.__product
    
    def setPassword(self,newEmail:str,oldEmail:str):
        if oldEmail == self.__email:
            self.__email == newEmail
        else:
            return
        
    def clearCart(self):
        self.__product.clear()
    

