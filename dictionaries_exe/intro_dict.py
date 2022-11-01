
# how to create 

# They are used to handle big data 

# The items in a dictionary (unlike lists or tuples)
# exists
# in a key and value pair

def dict_intro():
  myDict = {"Key" : "values","Lance" : 90,"Sid" : 80,}


  print(myDict)

  print(type(myDict)) 

  # printing the value of a particular key in a dict

  print(myDict["Key"])
# the number of items in a dict using len()

  print("Total items : ", len(myDict))

def loop_dict():
  myNewDict = {
    "lancelot" : 12,
    "stephen" : 13,
    "mario" : 14,
    "puzo" : 15,
      }

  # to loop through the entire dict
  for keys, values in myNewDict.items():
    print(keys, " : ", values, "\n")

  # to loop through the values only
  print(myNewDict.values())

# for more dict methods : https://www.geeksforgeeks.org/python-dictionary-methods/