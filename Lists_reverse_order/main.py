# Problem Statement 
# Given two python lists 'List1' and 'List2'
# Write a python program to iterate simultaniously 
# between both the lists to diplay the following output :
# List1 = ["Summer", "Winter", "Autmn", "Spring"]
# List2 = [1989, 1996, 1801, 2001]
# Output : Summer 1989
#          Winter 1996
#          Autmn 1801
#          Spring 2001

# ------------- Please start writing your solution from here ---------------- #

List1 = ["Summer", "Winter", "Autmn", "Spring"]

List2 = [1989, 1996, 1801, 2001]

for seasons, year in zip(List1, List2[::-1]):
  print("\n",seasons, "->", year, "\n")

# ------------- Explaination with example ---------------- #
# Python zip() method takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
# It is used to map the similar index of multiple containers so that they can be used just using a single entity. 

# Example :
name = [ "Laneclot", "Elliot", "Sid", "Labs" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print("\n", dict(mapped))