my_list = [10,10,20,30,30,40,50,50,60]
# Create empty list for to hold unique items
unique_items = []

# "For loop" that looks for items in list that are not in the empty list, then adds them to the empty list.
for items in my_list:
  if items not in unique_items:
    unique_items.append(items)

print ("my list", my_list)
print("unique items", unique_items)