"""Write a Python script to sort (ascending and descending) a dictionary by 
value. """

my_dict = {'a': 5, 'b': 3, 'c': 7, 'd': 1}
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("ascending order:",asc)
print("descending order:",desc)
