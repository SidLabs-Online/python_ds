# Problem Statement 
# Given two python lists 'List1' and 'List2'
# Write a python program to iterate simultaneously 
# between both the lists to display the following output :
# List1 = ["Summer", "Winter", "Autumn", "Spring"]
# List2 = [1989, 1996, 1801, 2001]
# Expected Output : Summer -> 1989
#          Winter -> 1996
#          Autumn -> 1801
#          Spring -> 2001

# ------------- Please start writing your solution from here ---------------- #

List1 = ["Summer", "Winter", "Autumn", "Spring"]

List2 = [1989, 1996, 1801, 2001]

for seasons, year in zip(List1, List2[::-1]):
  print("\n",seasons, "->", year, "\n")

# ------------- Explanation with example for zip() ---------------- #
# Python zip() method takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
# It is used to map the similar index of multiple containers so that they can be used just using a single entity. 

# Example :
name = [ "Lancelot", "Elliot", "Sid", "Labs" ]
roll_no = [ 4, 1, 3, 2 ]
 
# using zip() to map values
mapped = zip(name, roll_no)
 
print("\n", "Example#1 output ->", dict(mapped), "\n")

# ------------- Explanation with example for slicing in python---------------- #
# # syntax -> list_name[Start : End : StepSize]
# In Python, list slicing is a common practice 
# and it is the most used technique for programmers 
# to solve efficient problems. Consider a python list, 
# In-order to access a range of elements in a list, 
# you need to slice a list. One way to do this is to use the 
# simple slicing operator i.e. colon(:)

print("\n", "Example#2 output ->", "\n")
print("\n", name[0 : 3 : 1]) # to slice the first three elements from the list

# Leaving any argument like Initial, End or IndexJump blank will lead to the use of default
# values i.e 0 as Initial, length of list as End and 1 as IndexJump.

print("\n", name[0 : 3])

# to reverse a list 

print("\n", name[::-1])


