# for and while
# start---->last item?----->true or false
# for i in sequence(1,2,3):as sequence we can use here list,tuple,set,dic,range,file,string
#    print(i)
items=(1,2,3,4,5,67)
for i in items:
    print("round",i)
print('#'*40)
items=[1,2,3,4,5,"hii"]
for i in items:
    print("round",i)
print('#'*40)
for i in "harshika":
     print("round",i)
print('#'*40)
for i in range(5):#range(start,stop)end is not include because it start 0
   print("round",i)
print('#'*40)
for i in range(1,6):
    print("increment",i)
print('#'*40)
for i in range(0,6,2):
    print("increment",i)
print('#'*40)
files=['Report.csv','DATA.csv ','Final.text']
for file in files:
    file=file.strip().lower().replace("text",'csv')
    print(f"processing {file}")
print('#'*40)
for i in range(1,11):
    print(f"7 X {i} = {7*i}")
print('#'*40)
for i in range(1,7):
    print("*"*i)
print('#'*40)
for i in [6,5,4,3,2,1]:
    print("*"*i)