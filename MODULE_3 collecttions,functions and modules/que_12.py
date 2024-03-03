""" Write a Python program to convert a list of characters into a string. 
"""
def str1(c_list):
    return ''.join(c_list)

c_list = ['a', 'b', 'c', 'd', 'e']
result = str1(c_list)
print("List converted to string:", result)
print(type(result))
