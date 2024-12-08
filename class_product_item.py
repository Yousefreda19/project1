class product_item:
    def __init__(self):
      self._name_product=""
      self._price=""
      self._amount=""
    def set_name_product(self):
       self._name_product=str(input("please enter name of product"))
    def set_price(self):
       self._price=int(input("please enter price of product"))
    def set_amount(self):
       self._amount=int(input("please enter amount of product"))
    def get_name_product(self):
       return self._name_product
    def get_price(self):
       return self._price
    def get_amount(self):      
       return self._amount         