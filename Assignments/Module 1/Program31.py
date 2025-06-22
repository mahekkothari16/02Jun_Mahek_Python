# Program 31 : Write a Python program that manipulates and prints strings using various string methods. 

string = "Hello World, how are you all?"
# removes any whitespace 
print(string.strip())

# returns the string in lower case:
print(string.lower())

#returns string in upper case:
print(string.upper())

#replaces a string with another string 
print(string.replace("l","r"))

#splits the string into substrings
print(string.split(","))

#Capitalize only the first letter of the sentence
print(string.capitalize())

#Counts the word in the sentence
print(string.count("hello"))

#Checks if the sentence ends with something
print(string.endswith("."))

#Capitalize every letter of every word in the sentence
print(string.title())

