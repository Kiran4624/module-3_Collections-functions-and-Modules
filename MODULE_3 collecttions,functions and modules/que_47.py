"""Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}"""
def create(str1):
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

sample= 'w3resource'
result = create(sample)
print(result)
