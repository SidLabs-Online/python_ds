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
# import re

# def mask_cc():
#     cc_string = input("Type your CC number :")
#     sum_of_cc = sum(map(str.isdigit, cc_string))
#     mask_char = "*"
#     digits_to_hide = sum_of_cc - 12

#     out_cc = re.sub('\d', mask_char, cc_string, digits_to_hide)

#     return out_cc


# Version 2, without using any libraries
aList = []
def mask_cc():
    user_input = input("\nType your CC number :")
    if len(user_input) != 16:
        print("Incorrect CC number, it must be a 16 digit long number printed on your card")
        try_again = input("Would you like to try again ?(Y/N)")
        if try_again.lower() == 'y':
            mask_cc()
        else:
            return "Input Error"
            #raise Exception("None")
    elif len(user_input) == 16:
        
    
        for items in user_input:
            aList.append(items)
        
        for i in range(12):
            aList[i] = "*"
    else:
        print("Incorrect CC number, it must be a 16 digit long number printed on your card")
        try_again = input("Would you like to try again ?(Y/N)")
        if try_again.lower() == 'y':
            mask_cc()
        else:
            return "Input Error"

    res_list = "".join(aList)
    
    return res_list

