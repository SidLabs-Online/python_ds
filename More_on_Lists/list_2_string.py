# Write a Python program to
#  convert a list of characters into a string

my_list = ["m","a","r","i","s","s","a"]

def convert(my_list):
  
# Initialize empty string  
  new_string = ""

# Traverse items in list and add character to new string
  for x in my_list:
   new_string += x

# Return String  
  return new_string

print("my_list:",my_list)
print ("my_list as a string:",convert(my_list))          