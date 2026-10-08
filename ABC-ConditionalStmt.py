'''if rule--only one if for chain 2. alsways start with if 3. required 4 it is standalone'''
score=70
if score>=100:
    print("pass with disctination")
else:
    print("failed")
#ternary operator true if condition else false
print("A" if score>=100 else "failed")
grade="distnation" if score>=100 else "failed"
print(grade)
print("A" if score>=100 else "b" if score>=80 else "c" if score>=60 else "d")
print("#"*25)
# case match
country="United States"
match country:
    case "United States" | "USA":
        print("us")
    case "India":
        print("ind")
    case _:
        print("unknon country")