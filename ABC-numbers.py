# types-int,type, float,complex
# math operators =+ -/* ** % //
# rounding abs() round(), ceil(),floor() trunc()
#advance math sqrt() sin() cos() log()
# random -random() randint()
import math
import random
x=5
y=5.6
z=2+3j
print(type(x))
print(type(y))
print(type(z))
print(int(y))
print(2+3)
print(4-2)
print(4*5)
print(10/5)
print(4//7)
print(2**3)
print(4%2)#use for check odd and even based on remindaer o and 1
print(abs(-8.78905))
print(round(-8.96875))
print(math.ceil(-8.90765))

print(math.ceil(8.90765))
print(math.floor(0.34567))
print(math.trunc(8.90765))
print(random.random())
print(random.randint(1,10))
print(y.is_integer())
print(x.is_integer())
print(isinstance(x,int))
print(isinstance(y,int))

x22=random.randint(1,100)
if(x22%2==0):
    print(f"{x22} is even")
else:
    print(f"{x22} is odd")