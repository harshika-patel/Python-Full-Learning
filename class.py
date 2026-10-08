class Student:
    def __init(self):
        print("This is a student class")
    def __init__(self,name):
        self.name=name
        print("This is a student name ",self.name)
    def get_name(self):
        return self.name
stu2=Student("vinay")
stu1=Student("harshika")
print(stu1.get_name())

# types of constructors-self parameter it called default constructor 
# and parameterized constructor -when we pass the parameter to the constructor it is called parameterized constructor 
# for example in the above code we have created a parameterized constructor and we have passed the name parameter to the constructor
#  and we have used self parameter to access the name parameter in the class