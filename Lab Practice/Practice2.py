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


#Bank Management System - 1)Account Opening:a/c number,a/c holder name,a/c type
                        # 2) Deposit:-Min withdrawal amount 2000
                        # 3) Withdrawal : id withdrawal money is less than balance error
                        # 4) Statement : a/c Number,a/c holder name, a/c type, balance -print it

'''num = int(input("Enter the number of your account: "))
name = input("Enter your name: ")
type = input("Enter the type of account you want to open ('savings account,personal account')").lower()

def opening():
    if type == 'savings account' or type=='personal account':
        print("Account Number: ",num)
        print("Account Holder Name: ",name)
        print("Account Type: ",type)
    else:
        print("Enter valid account")
opening()
dep = input("Enter the amount that you want to deposit: ")
def deposit():
    dep1=int(dep)
    if dep1 < 2000:
        print("The amount should be greater than 2000.")
deposit()

def withdrawal():
    wd = input("Enter the amount you want to withdraw: ")
    wd1 = int(wd)
    
    if wd1 > dep:
        print("Amount should not be greater than the balance")
    else:
        print("Done withdrawal of:",wd1)
        Current_Balance = dep - wd1
        print("Current Balance: ",Current_Balance)

def statement():
    pass
'''

