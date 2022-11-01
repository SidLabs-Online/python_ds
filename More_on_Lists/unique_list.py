# Write a Python program to get 
# unique values from a list.


my_list = [10,10,20,30,30,40,50,50,60]

# Create empty list to store unique items
unique_items = []

# Iterates over list to find items not in unique items list and adds them.
for items in my_list: 
  if items not in unique_items:
    unique_items.append(items)

print("my list", my_list)
print("unique items",unique_items)    
