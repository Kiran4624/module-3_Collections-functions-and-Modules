""" Write a Python program to find the highest 3 values in a dictionary 
"""
def highest_values(dictionary, n=3):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    highest_values = sorted_dict[:n]
    
    return highest_values

my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

highest = highest_values(my_dict, n=3)

print("Highest 3 values in the dictionary:", highest)
