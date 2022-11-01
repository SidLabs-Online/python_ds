# Write a Python program to count the number of strings 
# where the string length is 2 or more and the first and 
# last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

words = ['abc', 'xyz', 'aba', '1221']

# User-defined function featuring a counter
def match_words(words):
  ctr = 0

# "For loop" that looks for words that are both more than 1 character in length and have identical 1st and last characters, then adds 1 to the counter for each match
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print("The number of strings featuring two or more characters with identical first and last characters is",match_words(words))
