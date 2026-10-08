print("control flow")
# conditional stmt-where you need to make dicision
# repeat somthing-loop
#cotrol flow---conditional stmt-if ,else, elif(make decision)
# values--True, False
#logical operator--and or not
# functions - bool() any() all() isinstance()
# comparision operator-== != < > >= <=
# Membership operators-in, not in
# identity operator-is ,is not
print(True)
print(False)
print(type(True))
print(bool(1213))#if somthing is in that it True
print(bool("hi"))
print(bool())#empty 
print(bool(0))#empty
print(bool(""))#empty
print(bool(None))#empty
print("="*25)
email=""
phone="123456"
username=""
# allows registration if any field is filled
print(any([email,phone,username]))
# allows registration if all field is filled
print(all([email,phone,username]))
print("="*25)
print(isinstance(123,int))
print(isinstance(True,bool))
print(isinstance("123",int))
print("="*25)
print(3>2)
print(10==10)
print(10!=10)
print("a"=="b")
print(3<4<8)
print(5<4<8)
age=20
print(18<=age<=30)
print(f"{"="*25}Logical Operators{"="*25}")
print(3<5 and 5<6)
print(3>5 and 5<6)
print(3<5 or 5<6)
print(3>5 or 5>6)
print(not 3<5)
print(not 3>5)
print(not not 3>5)
print("="*25)

print (5==5 or 8>5 and 6<4)
print ((5==5 or 8>5) and 6<4)
print("="*25)

print('a' in 'data')
print('har' in ['mar','xar','har'])
print('hAr' in ('mar','xar','har'))
print('hAr' not in ('mar','xar','har'))
print(1 in [1,2,3])
print("="*25)

a=[1,3,4]
b=[1,3,4]
print(a==b)
print(a is b)
print(a is not b)
c=6
d=6
print(c is d)
print(c is not d)
# a is same identity of b
print("="*25)

user_name="hars"
age=20
print((user_name is not None and user_name!="") and age>=18)
print("="*25)
password="harshika"
print(len(password)>=8 and (" " not in password))
print("="*25)
user_email="har@gmail.comm"
print((user_email is not None and user_email!="")and ('@' in user_email)and (user_email.endswith(".com")))
user_name="harsdfgt123"
print((isinstance(user_name,str))and (user_name is not None and user_name!="") and (len(user_name)>5))
print("="*25)
user="admin" 
is_banned=False
is_correct_email=False
print((user=="admin" or user=="moderator") and (is_banned is True or is_correct_email is True))
