# there are 4 tyoes of functions--
'''1.buit in fucntions-such as print,len, input, type,str many more --it come with python so we do not need to do anything just use it 
2.Standard library function,it is so advance, it developed by python Team but for their use we need to import them , 
            for exam math, and random--so we import it and use it
3. external Library--community library-which is developed or writeen by community and for their use we need install them in our system and use them 
            as example, metplotlib, numpy,pandas
4. user-defined functions- which is buid by us - we build write logic and use them'''

# function has function defination where we write function logic and second is function call
def function_name():#function defination
    print("hello")
function_name()#function call

def multiplication(x):# x is here parameter - it called place holder also, it come in function defination
    print(x*2)
multiplication(3)# 3 is actual value or real vaule --it called arguments

# Functions define m,ultiple ways
# 1. no input and no return value or output
# 2. you pass input or parameter but no return value means no output
# 3.you pass single single parameter and return the output
# 4. you pass multiple parameter or input and received multiple output

Pi=3.14#global variable--which we declared at outside the function which accessible in whole class any where
def piMultiplication(y):
    z=2#local variable which is declared inside the function and use only inside the class , not at other place 
    print(Pi*y*z)
piMultiplication(2)

def clean_name(name):#name is Parameter here anme is raw data
    cleaned=name.strip().lower()# cleaned is processed data and it called local variable 
    print(cleaned)
clean_name(" HarShika    ")

def data(firstName, lastName):
     first=firstName.strip().lower()
     last=lastName.strip().lower()
     full_name=first+" "+last
     print(full_name)
data("Harshika","Patel")

# we have positinal arguments and keyword arguments
# positional arguments-values pass to the function based on their order
#keyword arguments-values pass to the function based on their Names

def data(firstName, lastName,country):
     first=firstName.strip().lower()
     last=lastName.strip().lower()
     full_name=first+" "+last
     print(full_name,country)
data("Harshika","Patel","Canada")
data("Canada","Patel","Har")#it called positional arguments'--in that we can put value by mistakly in wrong postiton
data(firstName="Vinay",lastName="Patel",country="USA")# it reduce the risk of positional arguments and it called keyword arguments

# mixed argument
data("Maria",lastName="Patel",country="USA")# you can use mixed arguments but it has rule ==start with positinal arguments 


#default Parameter
# parameter  that has already a value so if you dont pass anything in python uses that value automatically
def data(firstName, lastName,country='n/a'):# country='n/a' it default value
     first=firstName.strip().lower()
     last=lastName.strip().lower()
     full_name=first+" "+last
     print(full_name,country)
data("kumar",lastName="Patel")

# *args and **kwargs-keyword arguments
    # allows functions to accept a unknown number of arguments

def total(a,b):
    print(a+b)
total(2,3)
# total(2,3,4)# getting error here because in function we have only two agruments, 
# if we want run this line we need to go to fucntion and add parameter 3rd,likweise we need other add 
def total(*args):#when we used *args when we have similar values for example only number, only strings
    print(type(args))
    print(sum(args))
total(1,2,3)

#when we have different type of values means str, number ,bool, None togther - use **kwargs -
# -here we need to add key for their value because it type is dictionary
def user(**kwargs):
    print(kwargs)
    print(type(kwargs))
user(firstName="Harshika",lastNAme="Patel",age=25,year=1996,Country="USA")

#return
f=3
def multi_factor(x):
    y=x*f
    return y
ans=multi_factor(4.5)#here we store our fuction output and on that perform different operation such as print it , round or any others
print(ans)
print(round(ans))

def clean_name(name):#we can use the multiple return also
    if not name:
        return None
    cleaned=name.strip().lower()# 
    return cleaned
cleanData=clean_name(" HarShika    ")
print(cleanData)
cleanData1=clean_name("")
print(cleanData1)

def clean_name(name):
    lo_cleaned=name.strip().lower()
    up_cleaned=name.strip().upper()
    return lo_cleaned,up_cleaned#return multiple values also
output=clean_name(" HarShika  ")
print(type(output))
print(output)

lowCase,UpCase=clean_name(" HarShika  ")
print(type(output))
print(lowCase)
print(UpCase)


# function is clssify by it purpose and it use case
#1.........Action Functions(this all is different Name--side effect functions,handler, command function,service functions)-
# action function means it perform some action such as print, connect to the database,send email, call API

def write_log(msg):
    with open("app.log","a") as f:
        f.write(msg+"\n")
# write_log("App Started")
write_log("User_looged")
write_log("APp stooped")

#2.....Transformation function---raw data goes in, get transformed and returns processed data
# Data manipulation

def cleaned_email(email):
    lo_email=email.lower().strip()
    username=lo_email.split("@")
    return username
usernam,domain_name=cleaned_email("har@gmail.com")
print(f"UserName={usernam}\nDomain_Name={domain_name}")

def cleaned_email1(email):
    lo_email=email.lower().strip()
    username,domain=lo_email.split("@")
    return {"username":username,"Domain":domain}
cleanedData=cleaned_email1("har@gmail.com")#get output in dictioinary data structure
print(cleanedData)

#validation Functions-validate a condition and returns a boolean result (True and False)

def password_len(password):
    if len(password)>=8:
        return True
    return False
a=password_len("harshik")
a1=password_len("harshika123")
print(a)
print(a1)


def valid_email_format(email):
   return  '@' in email and email[0].isalpha and '.' in email
   
a=valid_email_format('har')
print(a)
a1=valid_email_format('har@gmail.com')
print(a1)

#orchestrator function--

# connect all type of function in one fuction called orchestator function

def process_user_email(email):
    write_log("-----------------------------------")
    write_log("App started")
    if not valid_email_format(email):
        write_log(f"invalid email received {email}")
    else:
        clean_email111=cleaned_email1(email)
        write_log(f"proccedd Email: {clean_email111}")
    write_log("App stopped")
email=input("Enter the email: ")
process_user_email(email)

