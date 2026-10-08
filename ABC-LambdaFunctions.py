#Lambda Functions is Anonymus function because it does not have name
#lambda mostly use with map,filter,sorted-for complex task

# output=lambda input :expression

multiply=lambda x:x*2
print(multiply(2))

add=lambda x,y:x+y
print(add(1,2))

check=lambda i:i in "harshika"
print(check('k'))
print(check('z'))


# lambda +map
# map(function,iterable)--to apply to whole data structure list
prices=['$12.40','$9.99','$100.00']
# p1='$12.40'
# print(p1.replace('$',''))
# print(type(p1.replace('$','')))
# print(type(float(p1.replace('$',''))))
# print(type(p1.replace('$','')))
lambda p:float(p.replace('$',''))#this is our functions
map(lambda p:float(p.replace('$','')),prices)
print(list(map(lambda p:float(p.replace('$','')),prices)))

# lambda+filter
price=[120,30,300,80]
# p>=100
print(price)
print(list(filter(lambda p:p>=100,price)))

# nested loop
students=[['maria',60],['har',90],['vinay',100]]
# s[1]>70
print(list(filter(lambda row:row[1]>70,students)))
print(list(filter(lambda row:row[0].startswith('m'),students)))

# lambda+sorted