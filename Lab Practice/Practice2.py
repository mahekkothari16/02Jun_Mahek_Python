#LIST
'''data = ["python","java","php","c++","js"]
print(data)

print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:3])

print(data)
print(len(data))
data[1]='ios' # value updates
print(data)

for i in data:
    print(i)

print(data.index("python"))
 
if "ios" in data:
    print("Yes")
else:
    print("No")

(data.append("Flutter"))
(data.insert(1,'ruby'))
print(data)
data.remove("python")
print(data)
data.pop()
print(data)'''

#del data
'''print(data)

mylist=data.copy()

#Dynamic List
city=[]
n = int(input("How many city you want to enter: "))
for i in range(n):
    x = input("Enter the name of the city: ")
    city.append(x)
print(city)'''

#Set
'''st = {'a','b','c','d','e'}
print(st)
st.add('f')
st.update(['g','h','i'])
print(st)
st.pop()
print(st)
st.remove('a')
print(st)
st.clear()
print(st)
del st
print(st)

if 'a' in st:
    print('Yes')
else:
    print('No')

print(len(st))'''

'''st1 =set()
user = int(input("Enter the number of thing you want to add: "))
for i in range(user):
    x=input("Enter thing: ")
    st1.add(x)
print(st1)'''

#Dictionary 
'''data = {'id':1,'name':'mahek','sub':'python'}
print(data)
print(data['name'])
print(data.get("sub"))
print(data.keys())
print(data.values())

data["id"]=102
print(data)
data["city"]='Rajkot' #to add and also update
print(data)

for i in data.items():
    print(i)
for i in data.values():
    print(i)

for i,j in data,items:
    print(f"Key={i} and value={j}")

data.pop('sub')
data.clear()
del data
newdict=data.copy()
print(newdict)'''

#Dynamic dicitonary
'''print(dict)
dict = {}
user = int(input("How many pairs you want to add? "))
for i in range(user):
    kys=input("Enter the Key you want to add: ")
    value=input("Enter the value you want to add: ")
    dict[kys]=value
print(dict)'''

'''
data = {}
keys = ['id','name','city']
for i in range(len(keys)):
    v=input(f"Enter value of {keys[i]}:")
    data[keys[i]]=v
print(data)'''

'''stdata = [{'id':101,'name':'mahek'},
          {'id':102,'name':'tirth'},
          {'id':103,'name':'niyati'}]
print(stdata)
 
for i in stdata:
    print(i['name'])'''


#FUNCTION
'''def getdata(id,name):
    print("ID:",id)
    print("Name:",name)
dict = {}
n = int(input("Enter number of students: "))
for i in range(n):
    stid=input("Enter an ID:")
    stnm=input("Enter the name: ")
    getdata(stid,stnm)
    dict[stid]=stnm
print(dict)'''




'''def getdata(*data): #arbit argument
    print("ID:",data[0])
    print("Name:",data[1])
    print("City:",data[2])

getdata(101,'mahek','rajkot')
getdata(102,'niyati','ahmedabad')'''



'''def getdata(data): 
    print("ID:",data[0])
    print("Name:",data[1])
    print("City:",data[2])

getdata([101,'mahek','rajkot'])'''



#Random 
'''import random
x = random.random()
x = random.randint(11111,99999)
captcha = ['uiYx','Js0c','Jc0w','Ocmx','Jfmd']
x = random.choice(captcha)
print(x)

random.shuffle(captcha)
print(captcha)

'''

'''import math
print(math.pi)
print(math.e)
x = math.floor(78.56)
x = math.ceil(78.56)
x = math.pow(5,4)
x = math.factorial(5)
print(x)'''

'''import calendar
year = int(input("Enter any year: "))
x = calendar.calendar(year)
print(x)'''


'''import os
os.system('calc')
os.system('notepad')
os.startfile('chrome')
os.startfile('excel')
'''

'''import datetime
x = datetime.datetime.now()
print(x)
print("Day:",x.day)
print("Month:",x.month)
print("Year:",x.year)
print("Hours:",x.hour)
print("Min:",x.minute)
print("Second:",x.second)

'''

'''import platform
print(platform.architecture())
print(platform.machine())
print(platform.processor)
print(platform.python_version())'''


#import mylib
#from mylib import sum,sub
#import mylib as ml
'''from mylib import *

sum(34,53)
'''

#requests
'''import pandas as pd
import requests as rq
list = []
price=[]
url = "https://fakestoreapi.com/products"
req = rq.get(url)
data = req.json()

for i in data:
    info = ("Product ID:",i["id"],"Name:",i["title"],"Price of Product:",i["price"])
    list.append(info)
    price.append(i["price"])

print(list)
print(price)

df = pd.DataFrame(list)
print(df)

total=0
for i in data:
    #print(i["price"])
    total+=i["price"]

print("The total of price is:",total)
'''

#qrcode - for generating qrcode
'''import qrcode
url = ""
#url = "HI,hello students!How are y'll"
qr = qrcode.make(url)
qr.save("tops.png")'''

#-u yt-dlp
#pytubefix - for downloading youtube videos
'''from pytubefix import YouTube
url = "https://www.youtube.com/watch?v=3lDJZr6kbsg&list=RD3lDJZr6kbsg&start_radio=1"
YouTube(url).streams.first().download()
print("Download Successfully!")
'''

#pywhatkit for whatsapp messages
'''
import pywhatkit as pw
pw.sendwhatmsg_instantly("+918160939341","Hello Students!")
'''

#instaloader for downlaoding everything from public account of instagram
'''import instaloader
instaID=input("Enter any instagram's ID: ")
insta = instaloader.instaloader()
insta.download_profile(instaID)
print("Download Successfully")'''





