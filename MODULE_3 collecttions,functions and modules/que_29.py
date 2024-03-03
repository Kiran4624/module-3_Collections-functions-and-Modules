"""Write a Python program to unzip a list of tuples into individual lists. """
list1=[(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*list1)))