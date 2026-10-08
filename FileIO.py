#txt, csv ,json-for read and write we used file io function 
# open,operation(read,write,append),close file.delete file
# file operation-open,read,
# r-read mode
# w-write mode 
f=open("data.txt","r")#file object f varible store file object
data=f.read()
# data=f.readline()#read data by line by line
print(data)
print(type(data))
f.write("my name is HArshika")
# data=f.read()
# print(data)
f.close()# we always need to close our file explicitely


# --------------------------------------
# File operation
# r-reading-default--start to end-left to right
# w-writing,truncates file first-empty file fully no text on file 
# x-creates new and open for writing
# a-writing and appends at end
# b-binary Mode
# t-text mode-default
# +plus--opens disk file for update(r & w)

# read text-rt,wt-write text,rb-read binary, wb-write binary
# r+--read and write both perfroms , w+-read and write both((file became empty so it start from start)),
#  a+-read,append both(pointer at end)
# 