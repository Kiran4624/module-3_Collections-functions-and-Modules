"""Write a Python program to calculate the area of a parallelogram"""
def parallel(base, height):
    area = base * height
    return area

base_length = 6
height = 8
area = parallel(base_length, height)
print("Area of the parallelogram:", area)
