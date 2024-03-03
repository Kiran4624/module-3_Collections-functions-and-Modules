"""Write a Python script to merge two Python dictionaries """
def merge_(dict1, dict2):
    merge = dict1.copy()  
    merge.update(dict2)   
    return merge

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merge = merge_(dict1, dict2)

print("Merged dictionary:", merge)
