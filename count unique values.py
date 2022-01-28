# To count unique values in list+9

a=[6,6,7,8,9,9,6,7,4,3]

#Using set here as it doesnt allow duplicate values
c=list(set(a))
print(c) #Updated list with unique values
d=len(c)  #now taking count of elements in updated list
print(d)