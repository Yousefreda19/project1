from class_customerinfo import customer_info
import datetime
from main_meal import MainMeals
from sweets import sweets
from appa import Appetizers
from drink import Drinks
from order import order
class Bill:
    num_of_order=0
    def __init__(self):
        self .num_of_order+=1
        self.Total_price=0
        self.custtomer=customer_info()
        self.sweet=sweets()
        self.meal=MainMeals()
        self.drink=Drinks()
        self.order=order()
        self.appetizers=Appetizers()
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
     
