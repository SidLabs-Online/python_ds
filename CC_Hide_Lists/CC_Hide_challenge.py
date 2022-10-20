# Write a function 
# in Python that 
# accepts a credit 
# card number. 
# It should return a string
# where all the characters 
# are hidden with an 
# asterisk(*) except the 
# last four. 
# For example, 
# if the function 
# gets # sent "4444444444444444",
# then it should return "4444".
# 16 digits is a standard card length
# Sample outcome !
# input cc : 1234567890
# Hidden : ******8910
# Feature Update on october 20th 2022 : 
# Giving only 3 attempts to the user when 
# they make a mistake in typing the correct cc number 

# Solution without using any libraries 

aList = []

def masking(val):
    user_input = input("\nType your CC number :")
    val += 1
    if len(user_input) == 16:
        for items in user_input:
            aList.append(items)
        
        for i in range(12):
            aList[i] = "*"
        
        res_list = "".join(aList)
    
        print("\nMasked CC Number : ", res_list)

    elif len(user_input) != 16:
        print("\nIncorrect CC number, it must be a 16 digit long number printed on your card")
        try_again = input("\nWould you like to try again ?(Y/N)")
        if try_again.lower() == 'y':
            driver(val)
        else:
            return "Input Error"
            #raise Exception("None") 
    
    
    else:
        print("\nIncorrect CC number, it must be a 16 digit long number printed on your card")
        try_again = input("\nWould you like to try again ?(Y/N)")
        if try_again.lower() == 'y':
            driver(val)
        

    

def driver(attempt):
    if attempt > 2 :
        print("\nYou've exceeded the number of attempts\n")
    else:
        #attempt += 1
        print("\nAttempt # -> ", attempt+1, "\n")
        masking(attempt)
    
