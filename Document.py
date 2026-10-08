#Operatiors
'''1...Arithmetic Operators=+ - % / **--modulo operators(%)reminder of the division 
**--exponential operators a**b means a to the power of b=== 5**10=5*5*5*5*5*5*5*5*5*5=9765625

2...Relational Operators== != < > <= >=

3...Logical Operators === and or not 

4...Assignment Operators==,+=,-=,*=,/=,**=
bitwise operators== &,|,<<,>>,~,^
5...Membership Operators== in,not in
Operators precedence== 1...(),
2...**(exponential),
3...*,/,%,
4...+,-,
5...<,>,<=,>=,
6...==,!=,
7...not,
8...and,
9...or


type conversion== int(),float(),str(),bool()
type casting== implicit and explicit
implicit type casting== automatically convert one data type to another data type for example int to float
explicit type casting== manually convert one data type to another data type for example int to float ans=int(5+10.5) ans=15

USerinput== input() function is used to take input from the user and it always takes input in string format

1bit=0 or 1
1 byte = 8 bits
we count memory in bytes,generally laptop and desktop memory is measured in GB(1GB=1024MB) 
and maximum laptop and desktop memory is 64GB and 128GB,
and what the meaning of SSDD== solid state drive and HDD== hard disk drive what is the difference between SSD and HDD== SSD is faster than HDD
 because it has no moving parts and it uses flash memory to store data, while HDD has moving parts and uses magnetic storage to store data.
 and maximum SSD and HDD memory is 4TB and 16TB respectively
 if RAM and SSD HDD Memory is maximum then the laptop and desktop will be faster and it will take less time to open the application and it will be more efficient
 my variable store as bytes and 1kb=1024 bytes, 1MB=1024KB, 1GB=1024MB, 1TB=1024GB, 1PB=1024TB, 1EB=1024PB, 1ZB=1024EB, 1YB=1024ZB
 i have a=5 where it store as 4 bytes and b=10 where it store as 4 bytes and c=5.5 where it store as 8 bytes and d=True 
 where it store as 1 byte and e=None where it store as 0 bytes

 it store in catch memory and RAM memory is volatile memory 
 and it will be lost when the power is off and it is used to store data temporarily and it is used to store data that is currently being used by the CPU
1kb=1024 bytes
where permanent data is stored in hard disk drive and solid state drive and it is non-volatile memory 
and it will not be lost when the power is off and it is used to store data permanently

when i will buy latop what should i check as a developer good laptop for programming and development should have at least 8GB RAM, 256GB SSD,
 and a good processor like Intel i5 or i7 or AMD Ryzen 5 or 7. It should also have a good keyboard and display for comfortable coding experience.
'''

'''
int 4 bytes
float 8 bytes
sttring 1 byte per character
boolean 1 byte
long 8 bytes
'''


'''private attribute by double underscore __balance or__password 
we acces trhat by getter and setter create get_balance(self):
                                                return self.__balance--->objectName.get_balance()
we can accee trough class name also objectName._ClassName__PrivateAttribute

Protected Attribute ---is defined by single underscore _Name or _username and it is accessible by class object
OjectName._Name

Inhritance---to access the parents class method or init method we use super keyword for init method you use like this
super().__init__(name,salary)--parents class init method attributes 
super().speak()--this is parent class speak method in child class.
and if we have other parent class we need to acces it we can access through class name
Student.__init__(self,name)--likewise
'''



'''
Problem says...	Think Python...----
If / check / whether----	if
Otherwise	-----else
Multiple conditions----	elif
For every / each item----for
Repeat until-----	while
Store multiple items	----list
Unique items----set
Key-value information-----	dictionary
Does it exist?----	in
Doesn't exist?----	not in
Repeatable task	-----function
Count items	---counter / len()
Total	----accumulator / sum()
Largest/smallest-----	max() / min()'''