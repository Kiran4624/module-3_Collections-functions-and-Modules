"""Write a Python program to print all unique values in a dictionary."""
def unique(dictionary):

    unique_vals = set(dictionary.values())
    return unique_vals

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

unique_vals = unique(my_dict)

print("Unique values in the dictionary:", unique_vals)
