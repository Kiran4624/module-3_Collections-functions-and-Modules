"""Write a Python program to get unique values from a list"""
def unique(list1):
    return list(set(list1))

list1 = [1,2,1,3,2,4,5]
result = unique(list1)
print(result)
