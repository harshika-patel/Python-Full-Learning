import os
with open ("data.txt","r") as f:
  
    data=f.read()
    print(len(data))
os.remove("data3.txt")
    #delete file os module-operating system