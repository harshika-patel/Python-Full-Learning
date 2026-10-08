
import copy
# creat a empty list
empty=[]
print(empty)
print(type(empty))
letters=['a','b','c']#behind the scene 
# in memeory create a seperate object to store letters valuye object str=a, object str=b, object str=c, all has different addrss
numbers=[1,2,3]
mixed=[1,'a',None,True]
print(letters)
print(type(letters))
#build in functions list() -convert any data in list using list()
str="Data"
ls=list(str)
print(ls)
print(type(ls))


matrix=[[1,2,3],[2,4,5]]
print(matrix)
print(type(matrix))
print('*'*50)
mixed_matrix=[[1,2,3],['a','b'],[True]]
print(mixed_matrix)
print(type(mixed_matrix))
print('*'*50)

#how to access and read-indexing and sliceing
lst=['a','b','c','d']
print(lst[3])
print(lst[0:-1:3])#slicing lst[first:end:step]default first is 0 index end is last index
print(lst[1:])
print(lst[1:2])

print('*'*50)
mixed_matrix=[[1,2,3],
              ['a','b'],
              [True,1,2,3]]
print(mixed_matrix[2][0])
print(mixed_matrix[1][1])
print(mixed_matrix[2])
print(mixed_matrix[:2])
print(mixed_matrix[1:])
print(mixed_matrix[2][:2])
print('*'*50)

print(mixed_matrix[1:3][0:2])

print('*'*50)
# unpacking here
person=['maria','data engineer', 26, 'india']
# name=person[0]
# role=person[1]
# age=person[2]
# country=person[3]#here we write code in multile line but simple way is
name,role,age,country=person
print(name)
print(age)

# i am only intrested in 1st and last items 
print('*'*50)
person1=['maria','data engineer',9.4, 26, 'india']
name,*details,country=person1
print(name)
print(country)
print(details)

print('*'*50)
person2=['maria','data engineer',9.4, 26, 'india']
name,*details=person2
print(name)
print(details)

print('*'*50)
person3=['maria','data engineer',9.4, 26, 'london']
*details,country=person3
print(country)
print(details)

print('*'*50)
# Rule:numbers of values is matches with numbers=[1,2,3,4] list has 4 value than
#  we need to give "first,second, third, last=numbers"--this unpacking
str="harshjika"
firstLetter,*remainingLetters=str
print(firstLetter)

# underscore_--we do not care about that value where we put underscore
person4=['mani','data engineer',9.4, 26, 'spain']
name,_,_,_,country=person4
_,role,*details,country=person4
print(role)
print(country)
print(details)


print('*'*50)
person5=['mani','data engineer',9.4, 26, 'spain']
name,_,_,_,country=person5
_,role,*_,country=person5
print(role)
print(country)
print(name)

# Analyze and explore the Data
# max()-find extreme high,
# min()-find extreme low,
# len()-find the length,
# sum()-find the total,
# all()--did everything pass?,
# any()-did somthing pass?
# .count()-how often some Value repeat
# .index('a')-where it appears
# in-check if it exist?
# is-check if same objects
# ==
# >
print('*'*50)

numbers=[1,5,2,4,5]
numbers2=[1,5,2,4,5]
print("Max: ",max(numbers))
print("Min: ",min(numbers))
print("Sum: ",sum(numbers))
print("Len: ",len(numbers))
print("all: ",all(numbers))
print("all: ",all([0,1,3]))
print("all: ",all([1,"",3]))
print("all: ",all(['a','b','c',1,3,4]))
print("any: ",any(numbers))
print("any: ",any([0,1,3]))
print("any: ",any([1,"",3]))
print("any: ",any(['a','b','c',1,3,4]))
print("any: ",any([0,""]))

print("count of 5",numbers.count(5))
print("index of 5",numbers.index(5))#1st occurence of 5 index value we get here

print("5 is in our list",5 in numbers)
print("5 is not in our list",5 not in numbers)

print(numbers==numbers2)
print(numbers<numbers2)

print(numbers is numbers2)#both list has same values but here is check the memory address 
# so address are different for both list so we get false as output

# chnaging list-new data add, old data remove it , update that data
# .append()-add data in end.
# insert()-specific position
# remove()-by value(serech that value-it remove 1st occuranbce of value),,by postion pop(position numer)
#clear()-all the items are delete
print('*'*50)
letters=['a','b','c','a']
twoD=[[1,2,4],['x','y','z']]
letters.append('d')
print(letters)
letters.insert(0,'X')#first postion number and value
print(letters)
print(twoD)
twoD.append([4,5,6])
print(twoD)
twoD[2].append(7)
print(twoD)
twoD[0].insert(2,3)
print(twoD)
letters.remove("a")
twoD.remove([1,2,3,4])
print("Remove",twoD)

twoD[0].remove('y')
print("Remove y",twoD)

print(letters)
letters.pop(0)
print(letters)
letters.pop()#default is last items so it remove last items if er did not give any value
print(letters)
letters.pop(1)
print(letters)
letters.clear()
print(letters)

print('*'*50)

# update our data

listtt=[1,2,3,4,-7,6]
matrix1=[[1,2,3,5],['a','b','c']]
print(listtt)
listtt[4]=7
print(listtt)
print(matrix1)
matrix1[-1]=[6,7,8]
print(matrix1)
matrix1[0][0]='-'
print(matrix1)

# How to order your data----sort()
print('*'*50)
l=[1,8,3,4,-7,6,-1]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
lm=[['m','d','n']
    ,['c','a','A']]
print(lm)
lm[0].sort()
print(lm)
lm.sort()
print(lm)
lm.sort(reverse=True)
print(lm)

print('*'*50)
# leave original list as it and change in copy of that list we used sorted methods
# sort()-sort list ascending to decending low-high
# sort(reverse=True)-high to low
#sored()-returns new soretd list (keeps originals)
# reverse()-flip list arround
# reversed()--flip list in new list and keep originals
letter=['a','q','k','b']
newlist=sorted(letter)
print(newlist)
newlist=sorted(letter,reverse=True)
print(newlist)
print(letter)

print('*'*50)
# flip the list arround
letter=['a','q','k','b',1,2,3]
print(letter)
letter.reverse()
print(letter)
newlist=reversed(letter)
print(newlist)
newlist=list(reversed(letter))
print("changes in new list ",newlist)
print("original list",letter)


print('*'*50)
# copy --keep original data and work only with copy data so we did not loose any data
letter=['a','q','k','b',1,2,3]
letter_copy=letter#this is reference so change inone change in both
print(letter)
print(letter_copy)
letter_copy.append('d')
print("  ")
print(letter)
print(letter_copy)

letter_copy=letter.copy()
letter_copy.append('z')
print("  ")
print(letter)
print(letter_copy)

matrix=[[1,2],[3,4]]
copy_matrix=matrix.copy()
copy_matrix.append([5,6])
copy_matrix[0].append('x')#it shallow copy  because it change in both original matrix and copy matrix 
print("  ")
print(matrix)
print(copy_matrix)

# first import the copy --import copt
matrix=[[1,2],[3,4]]
copy_matrix=copy.deepcopy(matrix)
copy_matrix.append([5,6])
copy_matrix[0].append('x')#its deep copy  because it change in only in copy matrix 
print("  ")
print(matrix)
print(copy_matrix)

# first import the copy --import copt
matrix=[[1,2],[3,4]]
copy_matrix=copy.copy(matrix)
copy_matrix.append([5,6])
copy_matrix[0].append('x')##it shallow copy  because it change in both original matrix and copy matrix 
print("  ")
print(matrix)
print(copy_matrix)

# is operator for copy
print("  ")
matrix=[[1,2],[3,4]]
copy_matrix=matrix#both references to same object
print("copy using asignment operator",copy_matrix is matrix)
copy_matrix=copy.copy(matrix)
print("copy using shallow copy method",copy_matrix is matrix)
print("shared list?",copy_matrix[0] is matrix[0])
copy_matrix=copy.deepcopy(matrix)
print("copy using deepcopy method",copy_matrix is matrix)


# Combining lists--+ , extend()
print("  ")
list1=[1,2,3]
list2=[4,5,6,7]
fulllist=list1+list2
print(fulllist)
print(list1*2)
fulllist=[list1,list2]
print(fulllist)
list2.extend(list1)
print(list1)
print(list2)
print("  ")
# output of zip method is tuple plus iterator
com=zip(list1,list2)
print(com)
com=list(zip(list1,list2,"hiii78"))
print(com)

# real time example
ids=[101,102,103]
names=['ali','sara','john']
print(list(zip(ids,names)))


#______________________________________________________________________________________________________
# How to iterators a list
# iterables and iterators both are object but we convert it in list,set, tuple
# list,set,string all are itrable
# itrator is help to us for iteration
#1st reason- we need for loop
# 2nd reason-save memory
# 3rd -speed and flexibility
print(" ")
letters=['a','b','c']
for l in letters:
    # print(l)
    print(l.upper())

print(" ")
letters=['a','b','c']
new_list=[]
for l in letters:
    new_list.append(l)
print(new_list)

print(" ")
letters=['a','b','c']
new_list=[]
for l in letters:
    new_list.append(l.upper())
print(new_list)


# we have enumerate(iterable)--it returns position and value both
print(" ")
letters=['a','b','c']
print(list(enumerate(letters)))

print(" ")
letters=['a','b','c']
print(list(enumerate(letters,start=1)))

print(" ")
letters=['a','b','c']
for index,value in enumerate(letters):
    print(f"{index} : {value}")

print(" ")
letters=['a','b','c']
print(list(reversed(letters)))

print(" ")
letters=['a','b','c']
nums=[1,2,3]
print(list(zip(letters,nums)))
for index,value in zip(letters,nums):
    print(f"{index} : {value}")


# data transformation-map itrator
print(" ")
# letters=['a','b','c']
num=['1','2','3']
print(num)
print(list(map(int,num)))
# print(letters)
letters1111 = ['Abc  ', '  bac', 'c']
p111=map(str.strip,letters1111)
l111=list(p111)
print(l111)