from class_customerinfo import customer_info
from meal_class import main_class, MainMeals, Appetizer, drink, sweet

class order:
    def __init__(self):
        self.num_order = 0
        self.new_order = customer_info()
        self.meals = MainMeals()
        self.sweet = sweet()
        self.drinks = drink()
        self.appetizer = Appetizer()
        self.list_order = []
        self.discount = 10

    def set_info(self):
        self.new_order.set_name()
        self.new_order.set_num() 
        self.x = self.new_order.get_num()
        self.y = self.new_order.get_name() 

    def get_info(self):
        print(self.x)
        print(self.y)    

    def orders(self, type):
        x = """
        1-Main Meals
        2-Sweets
        3-Appetizers
        4-Drinks
        Enter type of food:
        """
        if type == 1:
            self.order_food(self.meals)
        elif type == 2:
            self.order_food(self.sweet)
        elif type == 3:
            self.order_food(self.appetizer)
        elif type == 4:
            self.order_food(self.drinks)

    def order_food(self, food_type):
        food_type.display_items()
        ordering = int(input("Please enter the number of the food item: "))
        amount = int(input("Enter the amount you need: "))
        boo1=food_type.is_found(ordering,amount)
        
        
        if boo1==False :
           return self.order_food(food_type)
      
        
        m = food_type.get_list()
        food_details = [m[ordering-1][0], amount, m[ordering-1][1]]
        
        
        self.list_order.append(food_details)
        
    def deleted_list_order(self):
        for idx, item in enumerate(self.list_order):
            print(f"{idx + 1} - {item}")
        
        k = int(input("Enter the number of the item to delete: "))
        self.list_order.pop(k-1)

    def confirm_the_order(self):
        confirm = int(input("Confirm the order or update (1-confirm / 2-update): "))
        if confirm == 1:
            self.num_order += 1
            return 1
        elif confirm == 2:
            print("1- Add")
            print("2- Delete")
            update_choice = int(input("Add or delete? "))
            if update_choice == 1:
                self.orders()
            elif update_choice == 2:
                self.deleted_list_order()   

    def get_order_info(self):
        return self.list_order

