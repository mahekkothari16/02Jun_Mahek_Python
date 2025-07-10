#Example 17:  Write a Python program to convert two lists into one dictionary using a for loop. 
dict = {}
list1=['Id','Name','Age','Gender']
list2=[1,'Mahek',21,'Female']
for i in range(len(list1)):
    dict[list1[i]] = list2[i]
print(dict)
