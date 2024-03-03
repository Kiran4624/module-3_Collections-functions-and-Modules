"""Write a Python program to replace last value of tuples in a list."""
list1=[(1,2,3),(4,5,6),(7,8,9)]
print(list1)
print([t[:-1]+(100,)for t in list1])