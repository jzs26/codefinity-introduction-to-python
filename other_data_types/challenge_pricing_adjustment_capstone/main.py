grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
"Eggs": ("Dairy", 5.50, 30),
"Bread": ("Bakery", 2.99, 15),
"Apples": ("Produce", 1.50, 50)
}
#print(grocery_inventory)
Price_of_Eggs = grocery_inventory["Eggs"][1]
#print(Price_of_Eggs)
if Price_of_Eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] =(
    grocery_inventory["Eggs"][0],Price_of_Eggs -1, grocery_inventory["Eggs"][2])
else:
    print("The price of Eggs is reasonable.")
    
grocery_inventory.update({"Tomatoes": ("Produce", 1.2, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
stock_of_milk = grocery_inventory["Milk"][2]
#print(stock_of_milk)
if stock_of_milk <10:
        print("Milk needs to be restocked. Increasing stock by 20 units.")
        grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        stock_of_milk + 20)
else:
    print("Milk has sufficient stock.")
price_of_apples = grocery_inventory["Apples"][1]
#print(price_of_apples)
if price_of_apples >2:
    grocery_inventory.pop("Apples")
else:
    pass
print("Updated inventory:", grocery_inventory)