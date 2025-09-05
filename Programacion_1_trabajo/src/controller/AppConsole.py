from ..model.User import User 
from ..model.Clothes import Clothes
from ..model.Vehicle import Vehicle
from ..model.Tech import Tech 
from ..view.View import View
from ..utils.JsonHelper import JsonHelper
import re


class AppConsole:
    def __init__(self):
        self.json = JsonHelper('resources/users.json', 'resources/products.json')

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return re.match(r'^[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

    def ask_valid_email(self, prompt="Insert your email") -> str:
        while True:
            email = View.askString(prompt)
            if self.is_valid_email(email):
                return email
            View.printError("Invalid email")

    def Umenu(self, products, user: User, users):
        while True:
            match View.userMenu():
                case 1:
                    View.printProducts(products)

                case 2:
                    product_name = View.askString("What product are you interested in?")
                    prd = self.json.searchProduct(products=products, productName=product_name)
                    if not prd:
                        View.printError("Product doesn't exist")
                        continue

                    if View.askBool("Do you want to make a purchase?"):
                        user.BuyProduct(prd)
                        print("Product added to your bag!")
                        print("Your bag:", user.getProduct())
                        self.json.deleteProduct(products, prd)
                        self.json.updateUser(users, user)

                case 3:
                    print(user.getProduct())

                case 4:
                    return 2

                case 0:
                    return 1

                case _:
                    View.printError("Option not available")

    def Smenu(self, products, user: User):
        product_types = {
            "clothes": lambda: Clothes(
                name=View.askString("Product name"),
                price=View.askFloat("Price"),
                seller=user.getEmail(),
                color=View.askString("Color"),
                cloth=View.askString("Cloth")
            ),
            "tech": lambda: Tech(
                name=View.askString("Product name"),
                price=View.askFloat("Price"),
                seller=user.getEmail(),
                color=View.askString("Color"),
                model=View.askString("Model"),
                cpu=View.askString("CPU")
            ),
            "vehicle": lambda: Vehicle(
                name=View.askString("Product name"),
                price=View.askFloat("Price"),
                seller=user.getEmail(),
                color=View.askString("Color"),
                model=View.askString("Model"),
                cc=View.askString("CC")
            )
        }

        while True:
            match View.sellerMenu():
                case 1:
                    View.printProductsBySeller(products, user)

                case 2:
                    kind = View.askString("What kind of product do you want to sell? (Clothes - Tech - Vehicle)")
                    creator = product_types.get(kind.lower())
                    if creator:
                        product = creator()
                        self.json.saveProduct(products, product)
                    else:
                        View.printError("That kind of product doesn't exist")

                case 3:
                    return 2 

                case 0:
                    return 1 

                case _:
                    View.printError("Option not available")

    def logger(self, users: list):
        View.login()
        if View.askBool("Do you already have an account?"):
            return self.logIn(users)
        return self.registerUser(users)

    def logIn(self, users):
        while True:
            View.login()
            email = self.ask_valid_email()
            password = View.askString("Insert your password")
            user = self.json.searchUser(users, email, password)
            if user:
                return user
            View.printError("Invalid credentials")

    def registerUser(self, users):
        name = View.askString("Insert your name")
        email = self.ask_valid_email()
        password = View.askString("Insert your password")
        seller = View.askBool("Are you a dealer?")

        if self.json.searchUser(users, email, password):
            View.printError("User already exists")
            return None

        user = User(name=name, email=email, password=password, seller=seller)
        self.json.saveUser(users, user)
        return user
    
    def mainLoop(self):
        user, counter = None, 0
        while True:
            users = self.json.loadUsers()
            products = self.json.loadProducts()

            if counter < 1:
                user = self.logger(users)
                if not user:
                    continue
                counter += 1

            if user.seller:
                option = self.Smenu(products, user)
            else:
                option = self.Umenu(products, user, users)

            if option == 1:
                break
            if option == 2:
                counter = 0
