# data transformation-map itrator
print(" ")
# letters=['a','b','c']
num=['1','2','3']
print(num)
print(list(map(int,num)))
# print(letters)
letters = ['Abc  ', '  bac', 'c']
p=map(str.strip,letters)
p2=map(str.upper,letters)
l=list(p)
print(l)
print(list(p2))

# we need to remove letter or number from the data we used Filter()
letters=['a','b','','c',None,'d',False]
print(list(filter(None,letters)))
letters=['a','b','c','d','True','e',"123","45"]
print(list(filter(bool,letters)))
print(list(filter(str.isalpha,letters)))
print(list(filter(str.isalnum,letters)))
print(list(filter(str.isnumeric,letters)))
for i in filter(str.isalpha,letters):
    print("alpha va;ues from list",i)
# itrable means it is data structure who are itrable for example list, set, dict, tuple, string,range
# while itrator is function who process that data and product diffeent result map(),filter(),zip()that all are iterator