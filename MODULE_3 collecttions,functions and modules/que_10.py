"""Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30."""



square = [i**2 for i in range(1, 31)]

print("First 5 elements:")
print(square[:5])

print("Last 5 elements:")
print(square[-5:])
