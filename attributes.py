# class attributes belongs to class
# instance attributes belongs to instance of class
# what is instance of class== instance of class is an object of class and it is created by calling the class name 
# and it is used to access the attributes and methods of the class
# instance methods are methods that are defined in the class and they are used to access the attributes of the class and they are called by using the instance of the class
class Student:
    college="ABC College" # class attribute
    PI=3.14
    def __init__(self,name,age): # instance attributes
        self.name=name# instance attributes
        self.age=age
        self.PI=9.1
stu1=Student("rahul",30)
print(Student.PI)
print(stu1.name)
print(stu1.PI)