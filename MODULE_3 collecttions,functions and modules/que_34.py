"""Write a Python script to check if a given key already exists in a 
dictionary. """

my_dict = {'a': 1, 'b': 2, 'c': 3}

given_key = 'd'

if given_key in my_dict:
    print("exists in the dictionary.")
else:
    print("does not exist in the dictionary.")
