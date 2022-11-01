# write a python code that allows,
# 1 . store book prices in an immutable data structure
# 2 . store book name and author name in a dict
# 3 . allow users to access author name and price by
#  entering a book name 

from typing import List


book_price = (12, 13, 14, 15)

book_dict = {
  "Harry Potter" : "Joanne Rowling",
  "Python" : "Lancelot",
  "Java Script" : "Sid",
  "Business" : "Elliot"
}

def driver():
  
  user_book = int(input("What's the name of the book ? : \n 1 - harry potter\n2 - Python\n3 - JavaScript\n4 - Business\n\t:"))
  newList = list(book_dict.keys())
  
  #print(newList[1])
  if user_book >= 1 and user_book <= 4:
    print("Book : ", newList[user_book-1])
    print("Author : ", book_dict[newList[user_book-1]])
    print("Price : $", book_price[user_book-1])
  else:
    print("Sorry invalid choice, please try again!")
  # for keys in book_dict.keys():
  #   if user_book != keys:
  #     print("Sorry!\nThat's an invalid book name!")
  #     break
  #   else:
  
  #     break