
# how to create 

# They are used to handle big data 

# The items in a dictionary (unlike lists or tuples)
# exists
# in a key and value pair

def dict_intro():
  print("Creating a dictionary using `{}`")
  myDict = {"Key" : "values","Lance" : 90,"Sid" : 80,}


  print(myDict)
  print("\n Using the type() function\n")
  print(type(myDict)) 

  print("printing the value of a particular key in a dict")

  print(myDict["Key"])
  print("the number of items in a dict using len()")

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

def dict_methods():
  # Create dictionary
  my_dict = {'Name' : 'Adam' , 'Age' :  7 , 'Class' : 'First' }

  # Access entries
  print ("my_dict['Name']: ", my_dict['Name'])
  print ("my_dict['Age']: ", my_dict['Age'])

  # access a data item with a key, which is not a part of the dictionary, we get an error check it out
  # print ("my_dict['Girl']: ", my_dict['Emma'])

  # update dictionary items
  my_dict['Age'] = 9; # update existing entry
  my_dict['School'] = "programming school" # Add new entry

  print ("\n my_dict['Age']: ", my_dict['Age'])
  print ("my_dict['School']: ", my_dict['School'])
  print ("\n ")
  # delete elemets
  del my_dict['Name']  # remove entry with key 'Name'
  print (my_dict)
  print ("\n ")

  my_dict.clear()     # remove all entries in my_dict
  print (my_dict)
  print ("\n ")

  #del my_dict         # delete entire dictionary
  #print (my_dict)
  #print (my_dict['Name'])
  print(my_dict)






# for more dict methods : https://www.geeksforgeeks.org/python-dictionary-methods/