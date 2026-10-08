# json Modules-javascipt object notation-format
# key value 
# jason array we called here in python list
# json.loads()==jason string to python object
# json.dumps()====python object to json string
#
import json
json_str='{ "name":"harshika", "isTeacher":true}'
print(type(json_str),json_str)
py_obj=json.loads(json_str)#here javascipt convert in python
print(type(py_obj),py_obj)

python_object={ "name":"harshika", "isTeacher":True}
json_str1=json.dumps(python_object)
print(type(json_str1),json_str1)
d={
    "name":"harshika",
    "age":30,
    "isTeacher":True
}

with open("data.json","r") as f:
    py_obj=json.load(f)
    print(py_obj)
with open("data1.json","w") as f:
    json.dump(d,f,indent=10,sort_keys=True)
