#dictionary-key and value
# dictinary is ordered
#key duplicate is not possible 
my_dict={
    'a':10,
    'b':20,
    'c':30,
    'a':56,# key duplicate is not possible
    'd':10#value duplicate is possible
}
print(my_dict)
# print(my_dict[1])#indexing is not possible #dictionary is not indexed
print(my_dict['a'])#we can access it using keys
my_dict['c']=100
print(my_dict)#dictinay is mutable

# Special methods of dictionary
print('# special methods #'*8)
user={"id":1,'age':45,'city':'Navsari'}
print(user['city'])
# print(user['name'])#this  key is not exist in dict and it give us a error and break the flow so we have other method is get
print(user.get("age"))
print(user.get("name "))
print(user.get("name","unknown"))

print("age" in user)
print("name" not in user)

#view objects
print(user.keys())
print(user.values())
print(user.items())# lis of tuples 
print(user)# get in dictonary form
for u in user:
    print(u,user[u])
# instead of this is good
for key, value in user.items():
    print(key,value)

# how to change dictionary--Add,remove,update
user['name']='john'#add
print(user)
user['age']=50#update value
print(user)
user.update({"age":89,'city': 'spain'})# multiple items update together using update method
print(user)
user.pop("age")# it remove the age from the dictionary
print(user)
name=user.pop("city")
print(name)
salary=user.pop("salary","not found")
print(salary)
#user.pop()#it give the error it is not like that list it is not delete last items we wann delete last items we have another method
user.popitem()

print(user)

user={
    'ide':None,
    'name':None,
    'age':None,
    "city":None
}
user1=dict.fromkeys(['id','name','age','city'],None)
print(user1)

# real time use of application

# dICT comprehensions has 3 commoponents---key value expression, loop, and an optional condition
user={
    'ide':1,
    'name':'john',
    'age':30,
    "city":'Berlin'
}
user_string={
    key.upper():value.upper()#expression
    for key,value in user.items() #loop
    if isinstance(value,str)#filter
}
user_string={
    key:value.upper()#expression
    for key,value in user.items() #loop
    if isinstance(value,str)#filter
}
print(user_string)