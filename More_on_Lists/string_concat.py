# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

def challenge():
  my_list = ['D','C']
  n = 5
  new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
  print(new_list)


# More on string.format methods 

def scoreMap ():
  lance = 75
  stephen = 80
  george = 70

  output = "The scores are : \nLance: {}, \nStephen: {}, \nGeorge: {} "

  output = output.format(lance, stephen, george)

  print(output)