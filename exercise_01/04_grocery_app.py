# 4. Grocery App
# Write a programme that
# (1) Allows warehouse employees to enter a list of goods 
# (including names only - using a string separated by commas) that are available in his/her shop
# (2) Allows customers to check whether an item is in stock or not by inputting a name:
# just show “Available” or “Out of stock!” on screen
from apps.grocery_app import GroceryApp

print("___4. Grocery App___");
GroceryApp().perform()
