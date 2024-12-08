from class_customerinfo import customer_info
from main_meal import MainMeals
from sweets import sweets
from appa import Appetizers
from drink import Drinks
class order:
    def __init__(self):
        self.num_order=0
        self.new_order=customer_info()
        self.meals=MainMeals()
        self.swet=sweets()
        self.drinnks=Drinks()
        self.appaetizer=Appetizers()
        self.list_order=[]
        self.discount=10
    def set_info(self):
        self.new_order.set_name()
        self.new_order.set_num() 
        self.x=self.new_order.get_num()
        self.y=self.new_order.get_name() 
    def get_info(self):
         print(self.x)
         print(self.y)    
        
    def orders(self):
        x="""
1-Main Meals
2-sweets
3-Appetizers
4-Drinks
enter type food ::"""
        type=int (input(x)) 
        if(type==1):
           self.order_meal()
        elif (type==2):
             self.order_sweet()  
        elif(type== 3):
             self.order_appetizer()
        elif(type==4):
             self.order_Drink()            
           
           
    def order_meal(self):       
            self.meals.display()
            self.ordering=int(input ("please enter num of meal ::"))
            self.amount=int(input("enter amount you needs ::"))
            self.boo1=self.meals.isfound_item(self.ordering)
            self.boo2=self.meals.isfound_amount(self.ordering,self.amount)
            if self.boo1==0:
                print ("This item does not exist")
                self.order_meal()
            if self.boo2==0:
                print("This quantity is not available")
                self.order_meal()
            self.m=self.meals.get_list ()  
            self.b=[self.m[self.ordering-1][0],self.amount,self.m[self.ordering-1][1]]
            self.meals.decrease_quantity(self.amount,self.ordering)
            self.list_order.append(self.b)
                
    def order_sweet(self):       
            self.swet.display()
            self.ordering=int(input ("please enter num of meal ::"))
            self.amount=int(input("enter amount you needs ::"))
            self.boo1=self.swet.isfound_item(self.ordering)
            self.boo2=self.swet.isfound_amount(self.ordering,self.amount)
            if self.boo1==0:
                print ("This item does not exist")
                self.order_sweet()
            if self.boo2==0:
                print("This quantity is not available")
                self.order_sweet()
            self.m=self.swet.get_list ()  
            self.b=[self.m[self.ordering-1][0],self.amount,self.m[self.ordering-1][1]]
            self.swet.decrease_quantity(self.amount,self.ordering)
            self.list_order.append(self.b)
    def order_appetizer(self):       
            self.appaetizer.display()
            self.ordering=int(input ("please enter num of meal ::"))
            self.amount=int(input("enter amount you needs ::"))
            self.boo1=self.appaetizer.isfound_item(self.ordering)
            self.boo2=self.appaetizer.isfound_amount(self.ordering,self.amount)
            if self.boo1==0:
                print ("This item does not exist")
                self.order_appetizer()
            if self.boo2==0:
                print("This quantity is not available")
                self.order_appetizer()
            self.m=self.appaetizer.get_list ()  
            self.b=[self.m[self.ordering-1][0],self.amount,self.m[self.ordering-1][1]]
            self.appaetizer.decrease_quantity(self.amount,self.ordering)
            self.list_order.append(self.b)
    def order_Drink(self):       
            self.drinnks.display()
            self.ordering=int(input ("please enter num of meal ::"))
            self.amount=int(input("enter amount you needs ::"))
            self.boo1=self.drinnks.isfound_item(self.ordering)
            self.boo2=self.drinnks.isfound_amount(self.ordering,self.amount)
            if self.boo1==0:
                print ("This item does not exist")
                self.order_Drink()
            if self.boo2==0:
                print("This quantity is not available")
                self.order_Drink()
            self.m=self.drinnks.get_list ()  
            self.b=[self.m[self.ordering-1][0],self.amount,self.m[self.ordering-1][1]]
            self.drinnks.decrease_quantity(self.amount,self.ordering)
            self.list_order.append(self.b)
    
    def deleted_list_ordar(self):
         self.h=0
         while self.h<len(self.list_order)  :
              print(self.h+1,"-",self.list_order[self.h])
              self.h+=1                      
         self.k=int(input("enter num wanted deleted ::"))
         self.list_order.pop(self.k-1)
         
    def Confirm_the_order(self):
         self.confire=int(input("Confirm the order or update(1-confire/2-update) "))
         if(self.confire==1):
              self.num_order+=1
              return 1
         elif self.confire==2:
              print("1-add")
              print("2-delete")
              self.update=int(input("add or delete"))
              if self.update==1:
                   self.orders()
              elif self.update==2:
                   self.deleted_list_ordar()   
  
    def get_order_info(self):
         return self.list_order
 