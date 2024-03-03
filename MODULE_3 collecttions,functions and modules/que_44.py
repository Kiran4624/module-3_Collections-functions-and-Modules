"""Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']} 
Expected Output: 
ac ad bc bd"""
from itertools import product

def generate_combinations(data):

    combinations = product(*data.values())
    
    
    result = [''.join(combination) for combination in combinations]
    
    return result

data = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = generate_combinations(data)
print("All combinations:", ' '.join(combinations))
