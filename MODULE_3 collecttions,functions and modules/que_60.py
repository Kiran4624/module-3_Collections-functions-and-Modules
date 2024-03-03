"""Write a Python program to calculate the area of a trapezoid"""
def trapezoid_area(a, b, h):
    area = ((a + b) / 2) * h
    return area

side_a = 5
side_b = 7
height = 4
area = trapezoid_area(side_a, side_b, height)
print("Area of the trapezoid:", area)
