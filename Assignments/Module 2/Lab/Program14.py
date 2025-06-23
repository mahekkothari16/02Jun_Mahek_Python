# Program 14 : Write a Python program to merge two lists into one dictionary using a loop. 
dict = {}
list1=['Id','Name','Age','Gender']
list2=[1,'Mahek',21,'Female']
for i in range(len(list1)):
    dict[list1[i]] = list2[i]
print(dict)

