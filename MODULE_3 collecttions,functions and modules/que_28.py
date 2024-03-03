"""Write a Python program to remove an empty tuple(s) from a list of tuples. """
list1=[(1,2,3),(4,5),()]
for tup in list1:
    if(len(tup)==0):
        list1.remove(tup)
print(list1)