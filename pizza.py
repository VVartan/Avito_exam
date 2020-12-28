# -*- coding: utf-8 -*-
"""cli.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UY8T0MiUlBb_tQec6uTzlhf5gxCfgdyq
"""

class Pizza_baseline():
    
    def __init__(self,size, name):
        
        self.name = name
        self.size = size
        self._items = {"tomato_sauce": 100, "mozarella": 150 , "tomatoes": 20, "vetrichina": 90}
        
    @property
    def size(self, value):
         if value in ("XL", "L"):
              self.size = value
         else:
              raise ValueError("Pizza can be XL or L only, choose again")      
                
    def dict(self):        
        return self._items
    
    def __repr__(self):
        return self.__class__.__name_
    
    def __eq__(self, other):       
        return self.dict() == other.dict()
        
class Margherita(Pizza_baseline):
   
    def __init__(self, size):
        self.name = "Margherita"
        self._items_update({"small_tomatoes": 10})
        super().__init__(self._items_update, size, self.name)
                
class Pepperoni(Pizza_baseline):   
    
    def __init__(self, size):
        self.name = "Pepperoni"
        self._items_update({"mushromms": 10})
        super().__init__(self._items_update, size, self.name)
                
class Hawaiian(Pizza_baseline):

    def __init__(self, size):
        self.name = "Hawaiian"
        self._items_update({"pineapples": 100})   
        super().__init__(self._items_update, size, self.name)