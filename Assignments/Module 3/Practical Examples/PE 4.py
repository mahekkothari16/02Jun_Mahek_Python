# Example 4 :  Write a Python program to create a file and print the string into the file.
file_write = [
    "This is first line\n"
]
with open("file.txt",'w') as file:
    file.write(file_write)
