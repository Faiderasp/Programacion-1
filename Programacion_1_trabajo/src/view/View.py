class View:
    @classmethod
    def login(cls):
        print("-" * 50)
        print("\t\tLOGIN\t\t" \
              
        "")

    @classmethod
    def printThings(t:str):
        print(f"\t{t}")

    @classmethod
    def userMenu(cls)->int:
        print("""
---- \t MAIN MENU \t----
1. View all products
2. Buy a product
3. Show my products
4. Log out
                 
0. Exit\n              
""")
        answer = View.askInt("Insert your option")
        return answer

    @classmethod
    def sellerMenu(cls)->int:
        print("""
---- \t MAIN MENU \t----
1. View all my products
2. Sell a product
3. Log out

0. Exit\n              
""")
        answer = View.askInt("Insert your option")
        return answer

    @classmethod
    def printError(cls, text)->None:
        print(f"X - {text}!!")

    @classmethod
    def askString(cls, text)->str:
        while True:
            try:    
                answer = str(input(f"{text} -> "))
                return answer
            except:
                cls.printError("Please enter a valid answer")

    @classmethod
    def askInt(cls, text)->int:
        while True:
            try:    
                answer = int(input(f"{text} -> "))
                return answer
            except:
                cls.printError("Please enter a valid answer")

    @classmethod
    def askFloat(cls, text)->float:
        while True:
            try:    
                answer = float(input(f"{text} -> "))
                return answer
            except:
                cls.printError("Please enter a valid answer")

    @classmethod
    def askBool(cls, text)->bool:
        while True:
            answer = str(input(f"{text} (y/n) -> "))
            match answer:
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    cls.printError("Please enter a valid answer")
                
    @classmethod           
    def printProducts(cls, products)->None:
        print("---\t PRODUCTS \t---")
        for product in products:
            print(f"{' → '.join([str(k) + " : " + str(v) for k, v in product.items()])}")

    @classmethod
    def printProductsBySeller(cls, products, user)->None:
        print("---\t MY PRODUCTS \t---")
        for product in products:
            if product['seller'] == user.getEmail():
                print(f"{' → '.join([str(k) + " : " + str(v) for k, v in product.items()])}")

