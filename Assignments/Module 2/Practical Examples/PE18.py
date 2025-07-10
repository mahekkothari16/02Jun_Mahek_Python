#Example 18 : Write a Python program to count how many times each character appears in a string.
strg = input("Enter the word you want to check for: ")
dict = {}
for i in strg:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("Character frequency:")
for i, count in dict.items():
    print(f"'{i}': {count}")
