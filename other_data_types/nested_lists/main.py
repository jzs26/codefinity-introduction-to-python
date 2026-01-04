vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
#print(vegetables)
if "carrots" in vegetables:
    print("Carrots are already in the list.")
else:
    vegetables.append("carrots")
#print(vegetables)
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")
else:
    vegetables.append("cucumbers")
vegetables.sort()
print("Updated Vegetable Inventory:",vegetables)