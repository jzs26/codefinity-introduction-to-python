# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]
#print(candy1, candy2, dry_goods)
category1 = categories[0:11]
#print(category1)
category2 = categories[13:]
#print(category2)
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
#print(bubblegum_price, chocolate_price, pasta_price)
#"We have dairy and bakery items: " + dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5"
print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category1}")