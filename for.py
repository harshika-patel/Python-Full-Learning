# string="hello"
# for var in string:
#     if var=="h":
#         print("h is present in the string")
#     print(var)

'''when we use for loop and while loop any specific identification variable is used to iterate over the sequence of elements in the string 
and it will take each character of the string one by one and it will print the character in each iteration of the loop
when we use while loop we need to use a counter variable to iterate over the sequence of elements in the string and
 it will take each character of the string one by one and it will print the character in each iteration of the loop

 for loop is used when we know the number of iterations and while loop is used when we don't know the number of iterations means
 we have to use a condition to terminate the loop'''


'''range() function is used to generate a sequence of numbers and it takes three arguments start,stop and step
 start is the starting number of the sequence and it is optional and by default it is 0
 '''
# word="artificial intelligence"
# ans=0
# for var in word:
#     # print(var)
#     if var=="i" or var=="a" or var=="e" or var=="o" or var=="u":
#         ans=ans+1
# print("the number of vowels in the string is",ans)

# n=int(input("enter the number "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("the sum of first",n,"natural numbers is",sum)

# dict={"name":"harshika","age":20,"gender":"female"}
# print(" ")
# print(dict)
# print(" ")
# print(dict["name"])
# print(" ")
# print(dict.keys())
# print(" ")
# print(dict.values())
# print(" ")
# dict_vals=list(dict.values())
# print(dict_vals)


# s={1,2,3,4,5,1,2,3,4,5}
# print(s.add(6))
# print(s)
# print(s.remove(1))
# s.pop()
# print(s)
# s.clear()
# print(s)


info=[("harshika","math"),("vinay","science"),("sneha","math"),("priya","english"),("sneha","science"),("priya","math")]

dict1={}
for name,subject in info:
   if(dict1.get(name)==None):
       dict1.update({name:set()})
       dict1[name].add(subject)
   else:
       dict1[name].add(subject)
print(dict1)