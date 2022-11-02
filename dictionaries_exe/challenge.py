# write a python code that allows,
# 1 . store book prices in an immutable data structure
# 2 . store book name and author name in a dict
# 3 . allow users to access author name and price by
#  entering a book name 



book_price = (12, 13, 14, 15)

book_dict = {
  "Harry Potter" : "Joanne Rowling",
  "Python" : "Lancelot",
  "Java Script" : "Sid",
  "Business" : "Elliot"
}

def driver():
  
  book_index = int(input("Choose book : \n 1 - harry potter\n2 - Python\n3 - JavaScript\n4 - Business\n\t:"))
  newList = list(book_dict.keys())
  
  #print(newList[1])
  if book_index >= 1 and book_index <= 4:
    print("Book : ", newList[book_index-1])
    print("Author : ", book_dict[newList[book_index-1]])
    print("Price : $", book_price[book_index-1])
  else:
    print("Sorry invalid choice, please try again!")
  