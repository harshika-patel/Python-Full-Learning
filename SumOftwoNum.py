'''a=5
b=10
print(a+b,a-b,a%b,a/b,a**b)
print(a==b,a!=b,a<b,a>b,a<=b,a>=b)

print(5)
ans=int(5+10.5) 
print(ans)
A=int(input("enter the number"))# bydefault input() function is used to take input from the user and it always takes input in string format
#--typecast in int() function to convert string to integer
print(A)
Num1=float(input("enter the number1 "))
Num2=float(input("enter the number2 "))
avg=(Num1+Num2)/2
print("average of two number is",avg)
name=input("enter your name")
age=int(input("enter your age"))
print("hello",name,"your age is",age)
number=float(input("enter the number"))
print("integer part",int(number),"fractional part",number-int(number))''' 

#swap two numbers without using third variable 
a=int(input("enter the number1"))

b=int(input("enter the number2"))
print("before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping a=",a,"b=",b)