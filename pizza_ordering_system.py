#Pizza ordering system

def main():
    
    import csv, datetime

    #Superclass
    class Pizza(object):
        def __init__(self, type, price, ing_1, ing_2):
            self.type = type
            self.price = price
            self.ing_1 = ing_1  #ingredients
            self.ing_2 = ing_2

    class pizza(Pizza):
        def get_description(self):
            description = f"{self.type} has {self.ing_1} and {self.ing_2} inside."
            return description
        
        def get_cost(self):
            price = f"{self.type} is ${self.price}."
            return price

    pizza_1 = pizza("Margherita Pizza", 13.25, "mozzarella", "tomato")
    pizza_2 = pizza("Pepperoni Pizza", 18.75, "pepperoni", "sweetcorn")
    pizza_3 = pizza("Hawaiian Pizza", 23.45, "pineapple", "mozzarella")
    pizza_4 = pizza("Veggie Pizza", 15.50, "mushroom", "olive")

    class Decorator(object):
        def __init__(self, name, price, ing_1, ing_2):
            self.name = name
            self.sprice = price
            self.ing_1 = ing_1  #ingredients
            self.ing_2 = ing_2

    #subclass
    class Sauce(Decorator):
        def get_description(self):
            description = f"{self.name} has {self.ing_1} and {self.ing_2} inside."
            return description
        
        def get_cost(self):
            cost = f"{self.name} is ${self.sprice}."
            return cost


    sauce_1 = Sauce("Garlic Sauce", 2.0, "garlic", "cream") #sauces have defined
    sauce_2 = Sauce("Ranch Sauce", 2.5, "mayonnaise", "parsley")
    sauce_3 = Sauce("BBQ Sauce", 1.5, "ketchup", "vinegar")

    order = {"Name":"", 
            "TC no": "",
            "Pizza type": "",
            "Pizza sauce": "",
            "Total price": 0,
            "Credit card no": "",
            "Credit card password": "",
            "Date": ""}

    with open("menu.txt", "r") as menu:

        read_menu = menu.read()
        print(read_menu)
        
        order_type = input("Pizza: ")
        order_sauce = input("Sauce: ")

        if order_type == "1":
            order["Pizza type"] = pizza_1.type
            order["Total price"] += pizza_1.price
            print(pizza_1.get_description())
            print(pizza_1.get_cost())
        elif order_type == "2":
            order["Pizza type"] = pizza_2.type
            order["Total price"] += pizza_2.price
            print(pizza_2.get_description())
            print(pizza_2.get_cost())
        elif order_type == "3":
            order["Pizza type"] = pizza_3.type
            order["Total price"] += pizza_3.price
            print(pizza_3.get_description())
            print(pizza_3.get_cost())
        elif order_type == "4":
            order["Pizza type"] = pizza_4.type
            order["Total price"] += pizza_4.price
            print(pizza_4.get_description())
            print(pizza_4.get_cost())
        else:
            print("Undefined selection")
        
        if order_sauce == "1":
            order["Pizza sauce"] = sauce_1.name
            order["Total price"] += sauce_1.sprice
            print(sauce_1.get_description())
            print(sauce_1.get_cost())
        elif order_sauce == "2":
            order["Pizza sauce"] = sauce_2.name
            order["Total price"] += sauce_2.sprice
            print(sauce_2.get_description())
            print(sauce_2.get_cost())
        elif order_sauce == "3":
            order["Pizza sauce"] = sauce_3.name
            order["Total price"] += sauce_3.sprice
            print(sauce_3.get_description())
            print(sauce_3.get_cost())
        else:
            print("Undefined selection")
        
        order["Name"] = input("Enter your name: ")
        order["TC no"] = input("Enter your TC no: ")
        order["Credit card no"] = input("Enter your credit card no: ")
        order["Credit card password"] = input("Enter your credit card password: ")
        order["Date"] = datetime.datetime.now()
        
        #creating a file for database
        database = open("orders_database.csv", "a") 
        database.write(str(order))
        database.write("\n")
        database.close()
        
        print("*Your order has been placed.*")
        print("Details of your order are down below:\n")
        print("Customer Name:", order["Name"])
        print("Ordered Pizza:", order["Pizza type"])
        print("Ordered sauce:", order["Pizza sauce"])
        print("Total Price:", order["Total price"])
        print("Order Date:", order["Date"])

if __name__ == "__main__":
    main()