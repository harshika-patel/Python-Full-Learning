class Store:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Store.count+=1

    def get_info(self):
        print(f"product name is {self.name} and it price is {self.price}")

    @classmethod
    def get_count(cls):#class methods
        print(f"tootal products created ={cls.count}")

    @staticmethod
    def cal_discount(price,discount):
        final_priced=price-(discount*price/100)
        print(f"discounted price is {final_priced}")

p1=Store("tshire",500)
p1.get_info()
Store.get_count()
p1.cal_discount(p1.price,10)