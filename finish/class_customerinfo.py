class customer_info:
    def __init__(self):
        self._num=""
        self._name=""
    def set_num(self):
        try:
          self._num=int (input("please enter your phone number ::"))
        except ValueError:
            print("phone number is not true") 
            self.set_num()
    def set_name(self):
          self._name=str(input("please enter your name ::"))
          if not self._name.isalpha():
            print("name is not true")  
            self.set_name() 
    def get_num(self):
        return f"phone number ::{self._num}"
    def get_name(self):
        return f"name ::{self._name}"
