from class_customerinfo import customer_info
import datetime
from meal_class import main_class,MainMeals,sweet,Appetizer,drink
class Bill:
    num_of_order=0
    def __init__(self):
        Bill.num_of_order+=1
        self.Total_price=0
        self.custtomer=customer_info()
        self.sweet=sweet()
        self.meal=MainMeals()
        self.drink=drink()
        self.appetizers=Appetizer()
    def info(self):
        self.custtomer.set_name()
        self.custtomer.set_num()
        print("**********WeZo**********")
        print("num of order",self.num_of_order)
        print("------------------------")   
        print(self.custtomer.get_name())
        print(self.custtomer.get_num())
        print("------------------------")
        print(datetime.datetime.now())
        print("------------------------")
     
