#Exercise 2:  Shipping Calculator
item = input("Enter the name of the item: ")
item_price = float(input("Enter the price of the item: "))
item_quantity = int(input("Enter the quantity of the item: "))
item_total = item_price * item_quantity
print("The total price of the item is", item_total)
if item_total <= 200:
    shipping_cost = item_total + 50
else:
    shipping_cost = item_total 
    
final_price = shipping_cost  
if final_price > 500:
    after_discount = final_price * 0.9      
    print("The final price after discount is", after_discount)
else:
    print("no discount apllied The final price is", final_price)