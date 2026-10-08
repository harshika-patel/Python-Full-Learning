# break- it stops the loop immediately it jumps out and emds the loop right away
for i in (1,2,3):
    if(i==2):
        break
    print(i)
print("*"*40)
# COntinue---it skips one loop cycle without stooping tye loop ---skip this one and go next
for i in (1,2,3,4,5):
    if(i==2):
        continue
    print(i)
print("*"*40)
#pass-it is a placeholder where nothing happens for now just keep going do nothing
for i in (1,2,3,4,5):
    if(i==2):
        pass
    print(i)
print("*"*40)
days=['mon','sun','tue','wes','sat','fri','thu']
for day in days:
    if day in ['sun','sat']:
        continue
    print(f"Working days {day}")
print("*"*40)

emails=['data@gmail.com',
        'har@gmail.com',
        'drop table users;',
        'harrr@gmail.com']
for email in emails:
    if ';' in email:
        print("SQL injection here spo break the flow")
        break
    print(f"Processing email:{email}")
#else in loop---runs a block of code only if the loop finishes naturally , loop completed without breaks
for i in range(5):
    if(i==2):
        continue
    print(i)
else:
    print("end")


print("*"*40)
for i in range(5):
    if(i==2):
        break
    print(i)
else:
    print("end")
print("*"*40)

# missing value
names=["har","vinay","har","moni","None"]
for name in names:
    if (name is None) or name=="":
        print("found empty value")
        break
else:
    print(f"all names is found")

#check if all files are csv files
files=['text.csv','har.csv','data.csv','har.json']
for file in files:
    if not file.endswith('.csv'):
        print(f"file has other extension instead of csv and it is {file}")
        break
else:
    print("all file has csv extesnion")

print('*'*45)
#check we have duplicate file or not
files=['text.csv','har.csv','data.csv','har.json','har.csv']

for file in files:
    if files.count(file)>1:
        print("we found duplicate here",file)
        break
else:
    print("all are unique files")


for file in files:
    print(f"{file} {files.count(file)}")
        
for x in (1,2,3):
    for y in (1,2):
        print(x,y)
for year in (2026,2027):
    for month in ('jan','feb','march'):
        for date in range(1,32):
            print(f"{date}-{month}-{year}")
