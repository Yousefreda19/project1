class main_class:
    def __init__(self,name_meal,list_meal=None):
        self.name_meal=name_meal
        self.list=list_meal if list_meal else []
        self.counter=len(self.list)
    def add_item(self):
        name = input(f"Enter {self.name_meal} name: ")
        price = int(input("Enter price: "))
        amount = int(input("Enter amount: "))
        self.counter += 1
        self.list.append([name, price, amount, self.counter])
        print(f"{self.name_meal} added successfully.")
    def display_items(self):
        if not self.list:
            print(f"No items in {self.name_meal}.")
        else:
            for item in self.list:
                print("  ".join(map(str, item)))
    def delete_item(self):
        item_num = int(input(f"Enter {self.name_meal} number to delete: ")) - 1
        if 0 <= item_num < len(self.list):
            self.list.pop(item_num)
            print(f"{self.name_meal} deleted successfully.")
            self.update_numbers()
        else:
            print("Invalid item number.")            
    def update_numbers(self):
        for i, item in enumerate(self.list):
            item[3] = i + 1
        self.counter = len(self.list)
    def update_price(self):
        item_num = int(input(f"Enter {self.name_meal} number to update price: ")) - 1
        if 0 <= item_num < len(self.list):
            new_price = int(input("Enter new price: "))
            self.list[item_num][1] = new_price
            print("Price updated successfully.")
        else:
            print("Invalid item number.")    
    def update_quantity(self, increase=True):
        item_num = int(input(f"Enter {self.name_meal} number to update quantity: ")) - 1
        if 0 <= item_num < len(self.list):
            change = int(input("Enter quantity to increase/decrease: "))
            if not increase:
                change = -change
            self.list[item_num][2] += change
            print("Quantity updated successfully.")
        else:
            print("Invalid item number.")
class MainMeals(main_class):
    def __init__(self):
        super().__init__("Main Meal", [["meat", 122, 100, 1], ["chicken", 120, 100, 2]])
class sweet(main_class):
    def __init__(self):
        super().__init__("Sweet", [["Basbosa",1001,1000,1],["Kunafa",140,1000,2]]) 
class drink(main_class):
    def __init__(self):
        super().__init__("Drink", [["orange",60,100,1],["mango",50,100,2]])        
class drink(main_class):
    def __init__(self):
        super().__init__("Appetizer",[["tahini",15,1000,1],["Vegetable Salad",15,42,2]])                               
