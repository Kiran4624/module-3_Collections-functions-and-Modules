"""Write a Python program to read a random line from a file."""
import random

def read(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip() 

filename = 'example.txt'  
random_line = read(filename)
print("Random line from the file:", random_line)
