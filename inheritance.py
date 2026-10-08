#inheritance-reusing attributes abd method from parent class (base class)
class Employess:
    start_time=10
    end_time=6

class adminstaff(Employess):
    def __init__(self,role):
        self.role=role

class Accountant(adminstaff):
    def __init__(self, salary,role):
      super().__init__(role)
      self.salary=salary

ac1=Accountant(10000,"manager")
print(ac1.salary,ac1.role,ac1.start_time,ac1.end_time)#multiple level inhritance

class Teacher(Employess):
    def __init__(self,subject):
        self.subject=subject
t1=Teacher("math")

print(f"{t1.subject} and {t1.start_time} and {t1.end_time}")#sigle level inheritance
# types-single level inheritance, employee to techer
# multilevel inheritance---employee to adminstaff to account
print("#multiple inhertance--one class inherit 2 or more parent class data--")
class Teacher1:
    def __init__(self,salary):
        self.salary=salary
class Student:
    def __init__(self,gpa):
        self.gpa=gpa
class Student2:
    def __init__(self,rollno):
        self.rollno=rollno
class TA(Teacher1,Student,Student2):
    def __init__(self, salary,gpa,name,rollno):
        super().__init__(salary)
        Student.__init__(self,gpa)
        Student2.__init__(self,rollno)
        # super().__init__(gpa)
        self.name=name
t1=TA(10000,9.5,"harshika",21)
print(t1.salary,t1.gpa,t1.name,t1.rollno)