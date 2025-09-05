import json
from ..model.User import User
from ..model.Product import Product
from ..view.View import View

class JsonHelper:

    def __init__(self, usersFilepath:str , productsFilepath:str):
        self.__usersFilepath = usersFilepath
        self.__productsFilepath = productsFilepath

    def loadUsers(self)->list:
        with open(self.__usersFilepath, 'r+') as f:
            users = json.load(f)
            return [{k.replace("_User__", ""): v for k, v in u.items()}for u in users]

    def loadProducts(self)->list:
        with open(self.__productsFilepath, 'r+') as f:
            products = json.load(f)
            return products
        
    def saveUser(self, users:list, user:User)->None:
        with open(self.__usersFilepath, 'w') as f:
            users.append(user.__dict__)
            json.dump(users, f)
    
    def saveProduct(self, products:list, product:Product)->None:
        with open(self.__productsFilepath, 'w') as f:
            products.append(product.__dict__)
            json.dump(products, f)

    def deleteProduct(self, products:list, productToDelete:dict)->None:
        with open(self.__productsFilepath, 'w') as f:
            for product in products:
                if productToDelete['name'] == product['name']:
                    products.remove(product)
            json.dump(products, f)

    def updateUser(self, users:list, userToUpdate:User)->None:
        with open(self.__usersFilepath, 'w') as f:
            for user in users:
                if user['email'] == userToUpdate.getEmail():
                    for product in userToUpdate.getProduct():
                        if product not in user['product']:
                            user['product'].append(product)
            json.dump(users, f)

    @classmethod
    def searchProduct(cls, products:list, productName:str)->dict:
        for product in products:
            if productName == product['name']:
                return product
        return None
    
    @classmethod
    def searchUser(cls, users:list, email:str, password:str)->User:
        for user in users:
            if user['email'] == email:
                if user['password'] == password:
                    return User(name = user['name'], email = email , password = password, seller = user['seller'], product = user['product'])
        return None


        
