# try,except,else,finally--exception handling
try:
    x=int(input("enter the x: "))
    ans=10/x
 
except ZeroDivisionError:
    print("divide by 0 is not possible")
else:
    print(ans)
finally:
    print("end of python rpogram")