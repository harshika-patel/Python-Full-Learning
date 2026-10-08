# while loop-repeats a bloack of code -over and over as long as condition is True
i=int(input("enyter any number"))
while i<10:
    print("I love You",i)
    i+=1
# do agree or not
answer=""
while answer!="yes":
    answer=input("do you agree?(yes/no): ")
print("Thank you")
# while True
while True:
    x=input("enter any text: ")
    if x=='stop':
        break
print("end")


# # difference between for and while loops
# # for loops we use when we know a fixed sequence, predefined condition, no of iteration is known , processind data
# # simple, clear, safe and limited

# # while loops-- while is condition is true 
# # our condition, no of iteration is unknown, waiting for external event,
# # advanced , flexible,complex and risk
while True:
    password=input("enter password : ")
    if password=="12345":
        break
print("valid password")

# # python challenges
# #allow 3 attems
# yes print in 3 attemps glad we are on the same page
# otherwise 3 stricks you are out
attempts=0
while attempts<3:
    answer=input("do you agree?(yes/no): ")
   
    if answer=='yes':
        print("glad we are on the same page")
        break
    attempts+=1
else:
    print("3 stricks you are out")