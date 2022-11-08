# use the get() method to print the values for 
# model & year key's from the given dict 

# Challenge 3 
# Find out if a value i.e. 1999 exist 
# in a given dictionary

# Challenge 4 
# replace the key "color" with "paint"
# for the given dictionary

# Challenge 5
# From the given dict, 
# change molly's salary to 2000

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
  carDict['paint'] = carDict.pop('color')
  
  print(carDict)

def challenge_5():
  # Challenge 5
  # From the given dict, 
  # Change molly's salary to 2000

  sample_dict = {
    'emp1' : {'name' : 'Lance', 'Salary': 7000},
    'emp2' : {'name' : 'Steve', 'Salary': 5000},
    'emp3' : {'name' : 'Holly', 'salary': 8000},
    'emp4' : {'name' : 'Lewis', 'salary': 9000},
    'emp5' : {'name' : 'Molly', 'salary': 11000},
  }

  sample_dict['emp5']['salary'] = 2000

  print(sample_dict)



  