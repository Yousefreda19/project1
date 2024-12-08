from class_product_item import product_item
class Appetizers(product_item):
    def __init__(self):
        super().__init__()
        self.list_Appetizers=[["tahini",15,1000,1],["Vegetable Salad",15,42,2]]
        self.counter_of_Appetizers=len(self.list_Appetizers)
        self.num_Appetizer=0
    def add_Appetizer(self):
        self.set_name_product()
        self.na=self.get_name_product()
        self.set_price() 
        self.pr=self.get_price()
        self.set_amount()
        self.am=self.get_amount()
        self.num_Appetizer=self.counter_of_Appetizers
        self.counter_of_Appetizers+=1
        self.new_Appetizer=[self.na,self.pr,self.am,self.num_Appetizer+1]
        self.list_Appetizers.append(self.new_Appetizer)
    def display(self):
       if self.counter_of_Appetizers==0:
           print("Empty.")
       x=0
       while x<self.counter_of_Appetizers :
          print("  ".join(map(str,self.list_Appetizers[x])))
          x+=1
    def delet_Appetizer(self):
        self.item_deleted=int(input("Please Enter Num Item Wanted Deleted ::"))  
        self.list_Appetizers.pop(self.item_deleted-1)
        self.counter_of_Appetizers-=1
        print("Deletion process completed .")
        self.p=self.item_deleted-1
        while self.p<self.counter_of_Appetizers:
              self.list_Appetizers[self.p][3]-=1
              self.p+=1
    def decrease_quantity(self,x,y):
         self.x=x
         self.y=y
         self.list_Appetizers[self.y-1][2]-=self.x          
    def update_price(self):
            self.item=int(input("please enter num item wanted udate price ::"))
            if(self.item>0 and self.item<=self.counter_of_Appetizers):
                self.new_price=int(input("enter new price ::"))
                self.list_Appetizers[self.item-1][1]=self.new_price
            else:
                print("Is not found")
    def Increase_quantity(self):
            self.item=int(input("Please enter num item wanted increase amount  ::"))
            if(self.item>0 and self.item<=self.counter_of_Appetizers):

                self.Increase=int(input("Enter num of increase amount ::"))
                self.list_Appetizers[self.item-1][2]+=self.Increase
            else:
                print("is not found")   
    def decrease_quantity(self):
            self.item=int(input("please enter num item wanted decrease amount ::"))
            if(self.item>0 and self.item<=self.counter_of_Appetizers):

                self.dncrease=int(input("Enter num of decrease amount ::"))
                self.list_Appetizers[self.item-1][2]-=self.dncrease
            else:
                print("is not found")               

    def isfound_item(self,x1):
           if x1-1<=self.counter_of_Appetizers:
                return 1
           else:
                return 0
    def isfound_amount(self,x1,x2):  
         if x2<=  self.list_Appetizers[x1-1][2]:
               return 1
         else:
                return 0 
    def get_list(self):
         return self.list_Appetizers   