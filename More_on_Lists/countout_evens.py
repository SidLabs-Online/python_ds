# Write a Python program to print the numbers of a specified list after removing even numbers from it.
# Hint :
# if num % 2 == 0:

# print("Even Number")

my_list = [2,3,5,6,8,11,12,15,20]

# Traverses each item in list checking for divisibility by 2 and removes each item that meats condition
for x in my_list:
  if(x %2 == 0):
    my_list.remove(x)

print ("Items in list not divisible by two:",my_list)
    