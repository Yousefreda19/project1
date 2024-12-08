from class_customerinfo import customer_info
from main_meal import MainMeals
from sweets import sweets
from appa import Appetizers
from drink import Drinks
from order import order
from bill import Bill

class Board:
    def __init__(self):
        self.order = order()
        self.new_order = customer_info()
        self.meals = MainMeals()
        self.sweet = sweets()
        self.drinks = Drinks()
        self.appetizer = Appetizers()
        self.bill = Bill()
        self.orders_list = []
        self.l=[]
        self.total=0

    def start_program(self):
        while True:  
            print("Main Meal ::")
            self.meals.display()
            print("Sweet ::")
            self.sweet.display()
            print("Drink ::")
            self.drinks.display()
            print("Appetizer ::")
            self.appetizer.display()

        
            self.des = int(input("1-New order / 0-Exit /2-Manager board ::"))
            if self.des == 1:
                self.start_new_order()
            elif self.des == 0:
                if(len(self.l)==0):
                    print(" No orders ")
                    self.start_program()
                else:
                   break  
            elif self.des==2:
                self.manager()

        self.print_all_orders_and_bill()

    def start_new_order(self):
        
        self.order.orders()
        self.l = self.order.get_order_info()
        
        
        self.orders_list.append(self.l)
        
        
        print(f"New Order: {self.l[0][1]}  {self.l[0][0]}  {self.l[0][2]}")

    def manager(self):
       self.passward=12345678
       self.x=int(input("Please Enter Passward ::"))
       if(self.x==self.passward):
          print ("Hello Boss ")
          print("Main Meal ::")
          self.meals.display()
          print("Sweet ::")
          self.sweet.display()
          print("Drink ::")
          self.drinks.display()
          print("Appetizer ::")
          self.appetizer.display()
          print("Any type of food you want to modify or delete ?")
          self.choice=int (input("1-Delete / 2-Add / 3-Change price / 4-Change amount ::"))
          if self.choice==1:
              x="""
1-Main Meals
2-sweets
3-Appetizers
4-Drinks
enter type food ::"""
              type=int (input(x)) 
              if(type==1):
                 self.meals.delet_MainMeal()
              elif (type==2):
                self.sweet.delet_sweet()  
              elif(type== 3):
                self.appetizer.delet_Appetizer()
              elif(type==4):
                self.drinks.delet_Drink()

          elif self.choice==2:
              x="""
1-Main Meals
2-sweets
3-Appetizers
4-Drinks
enter type food ::"""
              type=int (input(x)) 
              if(type==1):
                 self.meals.add_MainMeal()
              elif (type==2):
                self.sweet.add_sweet()  
              elif(type== 3):
                self.appetizer.add_Appetizer()
              elif(type==4):
                self.drinks.add_Drink()
          elif self.choice== 3:   
              x="""
1-Main Meals
2-sweets
3-Appetizers
4-Drinks
enter type food ::"""
              type=int (input(x)) 
              if(type==1):
                 self.meals.update_price()
              elif (type==2):
                self.sweet.update_price()  
              elif(type== 3):
                self.appetizer.update_price()
              elif(type==4):
                self.drinks.update_price()
          elif self.choice==4:
             self.t=int(input("1-Increase_quantity/2-decrease_quantity"))
             if self.t==1:
              x="""
1-Main Meals
2-sweets
3-Appetizers
4-Drinks
enter type food ::"""
              type=int (input(x)) 
              if(type==1):
                 self.meals.Increase_quantity()
              elif (type==2):
                self.sweet.Increase_quantity()  
              elif(type== 3):
                self.appetizer.Increase_quantity()
              elif(type==4):
                self.drinks.Increase_quantity()
             elif self.t==2:   
              x="""
1-Main Meals
2-sweets
3-Appetizers
4-Drinks
enter type food ::"""
              type=int (input(x)) 
              if(type==1):
                 self.meals.decrease_quantity()
              elif (type==2):
                self.sweet.decrease_quantity()  
              elif(type== 3):
                self.appetizer.decrease_quantity()
              elif(type==4):
                self.drinks.decrease_quantity()
                

       else:
           print("Wrong Passward !!!!")
           print("Please Try Agian")
           self.manager()

   

    def print_all_orders_and_bill(self):
        
        self.order.Confirm_the_order()
        self.bill.info()
        print("\nFinal Orders:")
        print("Amount   Name  Price")
        x=0
       
        for order in self.orders_list:
            print(f"{order[x][1]}       {order[x][0]}        {order[x][2]}")
            self.total+=order[x][1]*order[x][2]
            x+=1
        print("-----------------------")
        print("The Total Price ::     ",self.total ,"EGP")
        print("Discount        ::",self.order.discount,"%")
        print("Must Be Paid    ::",self.total-(self.total*self.order.discount/100))
        print("------------------------------------------------")
       
        
        print("\n    The Bill has been printed successfully!   ")


x = Board()
x.start_program()