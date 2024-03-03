"""Write a Python function that takes a list and returns a new list with unique 
elements of the first list. """
def new(list1):
    return list(set(list1))

list1 = [1,2,1,3,2,4,5]
result = new(list1)
print(result)
