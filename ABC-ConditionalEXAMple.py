email=input("enter the email address: ")
# if email is not None and email!="":
#     if ('.' and '@') in email:
#         if email.count("@")>=1 and (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
#             if len(email)>254 and email.startswith(isinstance(email,int)) and email.startswith(isinstance(email,str)):
#                 print(email)
# else:
#     print("there is no email exist")
email=email.strip()
valid=True
if email=="":
    print("email can not empty")
    valid=False
if ('.' and '@') not in email:
    print("email must contain . and @")
    valid=False
if email.count("@")!=1:
    print("email must conatin atlest one @")
    valid=False
if not email.endswith((".com",".org",".net")):
    print("end is conatin .com , .org..net")
    valid=False
if len(email)>254:
    print("no loger than 254")
    valid=False
if not (email[0].isalnum() and email[-1].isalnum()):
    print("start and end with letter and nuber")
    valid=False
if valid:
    print("perfect email addrss")
