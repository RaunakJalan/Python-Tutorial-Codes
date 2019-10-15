# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:02:04 2018

@author: Raunak
"""

#EG: CART.py

from string import Template

'''

def main():
    
    cart = []
    cart.append(dict(item = "Coke", price = 10, qty = 2))
    cart.append(dict(item = "Cake", price = 250, qty = 1))
    cart.append(dict(item = "Fish", price = 300, qty = 4))
    
    # $ -> indcates place holder
    t = Template("$qty x $item = $price")
    
    total = 0
    
    print("Cart: ")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
        
    print("Total: "+str(total))
    '''
    
#we can handle template error using safe_substitute() method
   
#Creating custom delimiter i.e. using # instead of $ 
    
class MyTemplate(Template):

    delimiter = '#'
    
def main():
    
    cart = []
    cart.append(dict(item = "Coke", price = 10, qty = 2))
    cart.append(dict(item = "Cake", price = 250, qty = 1))
    cart.append(dict(item = "Fish", price = 300, qty = 4))
    
    # $ -> indcates place holder
    t = MyTemplate("#qty x #item = #price")
    
    total = 0
    
    print("Cart: ")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
        
    print("Total: "+str(total))




    
if __name__ == "__main__":
    main()
    