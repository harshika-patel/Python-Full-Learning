# Instance methods are compulsory self pararmeter
#class methods are created in methods
#static method means 
print("----------------------Instance  Methods-----------------------------")
class Laptop:
    storage_type="SSD"
    def __init__(self, RAM ,Storage):
        self.RAM=RAM
        self.Storage=Storage
    def get_info(self):#instance method--access instance attributes plus class attributes
        print(f"laptop has {self.RAM} and {self.Storage} and it storage type is {self.storage_type}")
l1=Laptop("16gb","512gb")
l2=Laptop("8gb","1024gb")
l1.get_info()
l2.get_info()
print("----------------------Class Methods-----------------------------")
class Laptop1:
    storage_type="SSD"
    def __init__(self, RAM ,Storage):
        self.RAM=RAM
        self.Storage=Storage
    @classmethod #decorator menas change the behaviour of that methods
    def get_storage_type(cls):#class method only access class attributes
        print(f"storage type= {cls.storage_type}")
        # print(f"laptop has {cls.RAM} and {cls.Storage}") #after we add decorations we are getting error here because we access instance attribute by class methods 

    def get_info(self):#instance method--access instance attributes plus class attributes
        print(f"laptop has {self.RAM} and {self.Storage} and it storage type is {self.storage_type}")
l1=Laptop1("16gb","512gb")
l2=Laptop1("8gb","1024gb")
l1.get_info()
l2.get_info()
l1.get_storage_type()

print("----------------------Static Methods-----------------------------")
class Laptop2:
    storage_type="SSD"
    def __init__(self, RAM ,Storage):
        self.RAM=RAM
        self.Storage=Storage
    @classmethod #decorator menas change the behaviour of that methods
    def get_storage_type(cls):#class method only access class attributes
        print(f"storage type= {cls.storage_type}")
        # print(f"laptop has {cls.RAM} and {cls.Storage}") #after we add decorations we are getting error here because we access instance attribute by class methods 

    def get_info(self):#instance method--access instance attributes plus class attributes
        print(f"laptop has {self.RAM} and {self.Storage} and it storage type is {self.storage_type}")

    @staticmethod# static methods
    def cal_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"discounted price={final_price}")

l1=Laptop2("16gb","512gb")
l2=Laptop1("8gb","1024gb")
l1.cal_discount(500,10)