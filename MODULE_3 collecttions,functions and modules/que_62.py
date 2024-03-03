"""Write a Python program to calculate surface volume and area of a 
cylinder"""
import math

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

cylinder_radius = 3
cylinder_height = 5

surface_area = cylinder_surface_area(cylinder_radius, cylinder_height)
volume = cylinder_volume(cylinder_radius, cylinder_height)

print("Surface Area of the cylinder:", surface_area)
print("Volume of the cylinder:", volume)
