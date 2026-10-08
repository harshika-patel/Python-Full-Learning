data=True
line=1
with open("data.txt","r") as f:
    while data:
        data=f.readline()
        print(data)
        if ("python" in data):
            print(f"we found the python word successfully on line{line} ")
            break
        line+=1