# polymorphism--multiple function with same name 
# operator overload--+ is work as sum and as concentation
print(1+2,"hello"+"word")
# function overriding--inhirtance exist 
class Emp:
    def get_desigantion(self):
        print("designation=emp")
class Teacher(Emp):
    def get_desigantion(self):
        print("designation=teacher")
t1=Teacher()
t1.get_desigantion()#here teacher method is called it called function overrriding  
# and function overriding only happen when inheritance is exist

#-------duck type----
# walks like duck and quacks like duck--in different classes make same name methods it called duck type becaue both has same work
#  so it walk like duck and quake like duck
class tech:
    def get_desigantion(self):
            print("designation=teacher1")
class accountant:
     def get_desigantion(self):
                 print("designation=accountant")
t1=tech()
t1.get_desigantion()
a1=accountant()
a1.get_desigantion()