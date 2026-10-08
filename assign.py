str=input("enter the string: ")
reverse=""
for var in str:
   reverse=var+reverse
print("the reverse of the string is",reverse)
if str==reverse:
    print("the string is palindrome")       
else:
    print("the string is not palindrome")
