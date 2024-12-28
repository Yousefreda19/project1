from class_customerinfo import customer_info
from meal_class import main_class, MainMeals, Appetizer, drink, sweet
from order import order
from bill import Bill
class Board:
    def __init__(self):
        self.order = order()
        self.new_order = customer_info()
        self.meals = MainMeals()
        self.sweet = sweet()
        self.drinks = drink()
        self.appetizer = Appetizer()
        self.bill = Bill()
        self.orders_list = []
        self.l = []
        self.passward = 12345678
        self.total = 0

    def start_program(self):
     while True:  
       while True:  
        print("Main Meal ::")
        self.display_items(self.meals)
        print("Sweet ::")
        self.display_items(self.sweet)
        print("Drink ::")
        self.display_items(self.drinks)
        print("Appetizer ::")
        self.display_items(self.appetizer)


        print("1-New order / 0-Exit / 2-Manager board ::")
        self.des = int(input("Enter your choice: "))  

        if self.des == 1:
            self.start_new_order()  
        elif self.des == 0:
            if len(self.l) == 0:
                print("No orders yet!")
            else:
                break  
        elif self.des == 2:
            self.manager()
        else:
            print("Invalid choice! Please enter 1, 0, or 2.")  

       self.print_all_orders_and_bill()

    def start_new_order(self):
        x = """1-Main Meals
2-sweets
3-Appetizers
4-Drinks
Enter food type:: """
        y=int(input(x))
        self.order.orders(y)
        self.l = self.order.get_order_info()
        self.orders_list.append(self.l)
        print(f"New Order: {self.l[0][1]}  {self.l[0][0]}  {self.l[0][2]}")

    def manager(self, y):
        self.x = int(input("Please Enter Passward ::"))
        if self.x == self.passward:
            print("Hello Boss ")
            print("Main Meal ::")
            self.display_items(self.meals)
            print("Sweet ::")
            self.display_items(self.sweet)
            print("Drink ::")
            self.display_items(self.drinks)
            print("Appetizer ::")
            self.display_items(self.appetizer)

            print("Any type of food you want to modify or delete?")
            self.choice = int(input("1-Delete / 2-Add / 3-Change price / 4-Change amount ::"))
            if self.choice in [1, 2, 3, 4]:
                x = """1-Main Meals
                       2-sweets
                       3-Appetizers
                       4-Drinks
                       Enter food type: """
                type = int(input(x))
                self.handle_food_action(self.choice, self.get_food_type(type))
        else:
            print("Wrong Password!!!!")
            print("Please Try Again")
            self.manager()

    def handle_food_action(self, action, food_type):
        if action == 1:
            food_type.delet_item()  
        elif action == 2:
            food_type.add_item()  
        elif action == 3:
            food_type.update_price() 
        elif action == 4:
            quantity_action = int(input("1-Increase Quantity / 2-Decrease Quantity: "))
            if quantity_action == 1:
                food_type.increase_quantity()  
            elif quantity_action == 2:
                food_type.decrease_quantity()  

    def display_items(self, food_type):
        food_type.display_items()

    def get_food_type(self, type):
        if type == 1:
            return self.meals
        elif type == 2:
            return self.sweet
        elif type == 3:
            return self.appetizer
        elif type == 4:
            return self.drinks

    def print_all_orders_and_bill(self):
        self.order.confirm_the_order()
        self.bill.info()
        print("\nFinal Orders:")
        print("Amount   Name  Price")
        x = 0
        for order in self.orders_list:
            self.print_order_details(order)
        print("-----------------------")
        print("The Total Price ::     ", self.total, "EGP")
        print("Discount        ::", self.order.discount, "%")
        print("Must Be Paid    ::", self.total - (self.total * self.order.discount / 100))
        print("------------------------------------------------")
        print("\n    The Bill has been printed successfully!   ")

    def print_order_details(self, order):
        for item in order:
            print(f"{item[1]}       {item[0]}        {item[2]}")
            self.total += item[1] * item[2]
#board=Board()

#board.start_program()
