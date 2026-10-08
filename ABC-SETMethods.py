# set methhods
a={10,20,30,40}
a.add(50)#added in randomly position
print(a)
a.update("hi")
a.update({1,2,3,4})# add multiple values together
a|={5,6}# short cut of update
print(a)
a.remove(20)# it remove the value
# a.remove(100)#this value is not in set and we try to remove it so it gives us a error and break the whole flow 
# so we have new method is discard
a.discard(10)
a.discard(100)
a.pop()# randomly remove any value
print(a)
print("#"*50)
# mathimatical methods
a={10,20,30,40}
b={30,40,50,60}
print(a.union(b))# give unique value form two set
print(a|b)#-short cut of above
print(a.intersection(b))# both set common value here is 30 and 40
print(a & b)#-short cut of above
print(a.difference(b))#show me the items which only present in a not in b so here 10,20 while 30,40 alreadu in b ---
# if change b.differenace(a) tha op--50,60
print(a - b)#-short cut of above
print(b-a)
print(a.symmetric_difference(b))#return everything which is unique but not shared one
# here 30,40 is shared so it excluded and and others 10,20,50,60 is return
print(b ^ a)

print("#"*50)
# relationship of two set
c={30,40,50,60,70}
d={90,80}
print(a.issubset(b))# a is fully contain in B
print(b.issubset(c))
print(c.issubset(b))
print(c.issuperset(b))
print(b.issuperset(c))
print(c.isdisjoint(d))#it is not have any shared items? if they have no shred items op-True and it has -False
print(a.isdisjoint(b))