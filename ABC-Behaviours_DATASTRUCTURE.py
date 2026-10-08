# list--it is ordered because it remember the exact position of the elemenent untill ypu changed 
# printed which order it has , no change -follow our ordered
# list duplicates allow 
# list are index - access any value using it position
# list are mutabvle - it is changable
# overala every thing allows in list
my_list=[10,20,30,10]
print(my_list)
print(my_list[2])#it is indexing
my_list[3]=50
print(my_list)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Tuple--it is ordered collection and it is not changed after creation-it is locaked and frozen
# it is ordererd,
# it allowed duplicated
# it is accessible by indexing
# tuple is unmutable --it is not changable
my_tuple=(10,30,20,10)
print(my_tuple)
print(my_tuple[3])
# my_tuple[3]=40# here we get eerro because tuple is unmutable data structure
# my_tuple.remove(10)
print(sorted(my_tuple))#as output in list so in tuple we can not changed anything


# ----------------------------------------------------------------------------------------------------------------------------------------

# Set{}-it is unordered collection of unique values
# it is unique, it not allowed duplicate
# in what form our data it is not printed in that form it is sorted by itsself so it is not ordered it is unordered
# it loos ir ordered but provide fast excution
# remove duplicate by itsself
# not indexed possible
# it is mutable
my_set={1,2,6,7,3,4,5,1,'abc','a','har'}
# my_set[7]
print(my_set)
# print(my_set[7])
my_set.remove('har')
print(my_set)