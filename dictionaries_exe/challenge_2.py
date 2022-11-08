# use the get() method to print the values for 
# model & year key's from the given dict 

# Challenge 3 
# Find out if a value i.e. 1999 exist 
# in a given dictionary

# Challenge 4 
# replace the key "color" with "paint"

carDict = {
  "brand" : "Ford",
  "model" : "Mustang",
  "year" : 1990,
  "color" : "blue"
}


def challenge_2():
  # write your solution here!
  print("Solution challenge 2: \n")
  print(carDict.get("model"))

def challenge_3():

  # write your solution here!
  print("Solution challenge 2: \n")
  if 1999 in carDict.values():
    print("The value 1999 exists" )
  else:
    print("The value 1999 does not exist")

def challenge_4():

  #write your solution here : 

  print(carDict)