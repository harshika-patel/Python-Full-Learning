text="i love python, python is my favrotite language, my friend love python"
text2="hello"
name="    harshika"
age=24
print(type(text))
print(text.count("python"))
print(text+" \n"+text2)
print(name+str(age))
print(f"My name is {name} and age is {age}")
print(f"{{this is me}}")
data="adam-32-usa"
print(data.split('-'))#store in list
print('ha'*3)#multiply  specific text number, operrator anything just put in quotes
print("="*14)
print(name[0:3])#end index not include it give us 0 to only
print(name[3:])
print(name[:-4])
print(name[0:8:3])
date="2026-10-08"
a=date.index("08")
print(f"month is {date[8:]}")
#lstrip-remove white space from left
#rstrip-remove white space from right
#Strip-remove white space from both
print(name.lstrip())
ls=" I love Egineering  ".strip()
print(ls)
ls2="I love Egineering  "
print(f"number of white space {len(ls2)-len(ls2.strip())}")
text3="Python PROGRAMMING"
print(text3.lower())
print(text3.upper())
serach="Email".lower()
dataaa="emAil".lower()
print(serach==dataaa)

datee="2026-feb-10"
print(datee.startswith("2"))
print(datee.endswith("10"))
print(datee.find("0"))
print(datee.find("feb"))
print('feb' in datee)

print('Feb' in datee)
phone1="+46-234-6789"
phone2="432346789"
print(phone1[phone1.find('-')+1:])
#isalpha- check it has only letter
name2="chgaki"
print(name2.isalpha())
print(phone2.isnumeric())