# abstraction-hiding internal details and showing only essential features
# abstract classes-blue print for other classes -part of abc modules abc-abstraction based classes
# Difference between abstraction and encapsulation is ---in encapsulation we decide which data we need to hide,
# but in abstraction we decide both which data we need to hide and which data we need to show to users.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class lion(Animal):
    def make_sound(self):
        print("Roar!")
l1=lion()
l1.make_sound()