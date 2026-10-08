#encapsulation  abstraction inheratance polymorphism
#encapsulation means wrapping data and functions into single unit
# whenevr we created a class it called encapsulation becaue it conatine method and attributes
# data hiding-public data -everywhere accessible
#  protected Attribute- inside the class plus in the sub classes
# private attribute-inside the class -no access outside the class
class BanKAccount:
    def __init__(self, name,balance,accountNo):
        self.name=name#publice
        self._balance=balance#protected attribute after adding _,, and double underscore front of the methods it private attribute
        self.__accountNo=accountNo#private attribute-data mangling--private attribute access by getter and setter
    def get_accountNo(self):#getter
        return self.__accountNo
    def set_accountNo(self,newAccountNo):#setter
        self.__accountNo=newAccountNo

b1=BanKAccount("harshika",10000,1234)
# print(b1.name,b1._balance,b1.__account_no) account_no is not accesible here becayse it is private here 
print(b1.name,b1._balance,b1.get_accountNo())
b1.set_accountNo(4567)
print(b1.name,b1._balance,b1.get_accountNo())
print(b1.name,b1._balance,b1._BanKAccount__accountNo)#private varible also access by class name