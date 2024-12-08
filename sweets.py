from class_product_item import product_item
class sweets(product_item):
    def __init__(self):
        super().__init__()
        self.list_sweets=[["Basbosa",1001,1000,1],["Kunafa",140,1000,2]]
        self.counter_of_sweeets=len(self.list_sweets)
        self.num_sweet=0
    def add_sweet(self):
        self.set_name_product()
        self.na=self.get_name_product()
        self.set_price() 
        self.pr=self.get_price()
        self.set_amount()
        self.am=self.get_amount()
        self.num_sweet=self.counter_of_sweeets
        self.counter_of_sweeets+=1
        self.new_sweet=[self.na,self.pr,self.am,self.num_sweet+1]
        self.list_sweets.append(self.new_sweet)
    def display(self):
       if self.counter_of_sweeets==0:
           print("Empty.")
       x=0
       while x<self.counter_of_sweeets :
          print("  ".join(map(str,self.list_sweets[x])))
          x+=1
    def delet_sweet(self):
        self.item_deleted=int(input("Please Enter Num Item Wanted Deleted ::"))  
        self.list_sweets.pop(self.item_deleted-1)
        self.counter_of_sweeets-=1
        print("Deletion process completed .")
        self.p=self.item_deleted-1
        while self.p<self.counter_of_sweeets:
              self.list_sweets[self.p][3]-=1
              self.p+=1
    def decrease_quantity(self,x,y):
         self.x=x
         self.y=y
         self.list_sweets[self.y-1][2]-=self.x          
    def update_price(self):
            self.item=int(input("please enter num item wanted udate price ::"))
            if(self.item>0 and self.item<=self.counter_of_sweeets):
                self.new_price=int(input("enter new price ::"))
                self.list_sweets[self.item-1][1]=self.new_price
            else:
                print("Is not found")
    def Increase_quantity(self):
            self.item=int(input("Please enter num item wanted increase amount  ::"))
            if(self.item>0 and self.item<=self.counter_of_sweeets):

                self.Increase=int(input("Enter num of increase amount ::"))
                self.list_sweets[self.item-1][2]+=self.Increase
            else:
                print("is not found")   
    def decrease_quantity(self):
            self.item=int(input("please enter num item wanted decrease amount ::"))
            if(self.item>0 and self.item<=self.counter_of_sweeets):

                self.dncrease=int(input("Enter num of decrease amount ::"))
                self.list_sweets[self.item-1][2]-=self.dncrease
            else:
                print("is not found")               
    def isfound_item(self,x1):
           if x1-1<=self.counter_of_sweeets:
                return 1
           else:
                return 0
    def isfound_amount(self,x1,x2):  
         if x2<=  self.list_sweets[x1-1][2]:
               return 1
         else:
                return 0 
    def get_list(self):
         return self.list_sweets     