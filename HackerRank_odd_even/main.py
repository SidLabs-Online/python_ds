# if n is odd - weird
# if n is even in range 2 to 5 - not-weird
# if n is even 6 to 20 - weird
# if even and greater than 20 - not weird

n = int(input ("Please enter the number : "))

if (n % 2 != 0): 
  print("Even - weird")
elif (n % 2 == 0): 
  if n >=2 and n<=5:
    print("Odd -Not Weird")
  elif n >=6 and n<=20:
    print("Odd -Weird")
  elif n > 20:
    print("Odd -Not Weird")  

# a number that is not completely divisible 
# by 2 is an odd number & vice versa
# "==" this means checking if equal to
# "!=" this means not equal to 
# "%" is a mod operator  
# to learn more about operators - https://www.w3schools.com/python/python_operators.asp


