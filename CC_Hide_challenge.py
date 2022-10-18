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
import re

def mask_cc():
    cc_string = input("Type your CC number :")
    sum_of_cc = sum(map(str.isdigit, cc_string))
    mask_char = "*"
    digits_to_hide = sum_of_cc - 14

    out_cc = re.sub('\d', mask_char, cc_string, digits_to_hide)

    return out_cc
