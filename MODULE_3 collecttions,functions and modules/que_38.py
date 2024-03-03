"""Write a Python program to check multiple keys exists in a dictionary """
def check(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

keys= ['a', 'c', 'e']

# Check if all keys exist in the dictionary
if check(my_dict, keys):
    print("All keys exist in the dictionary")
else:
    print("one key does not exist in the dictionary")
