"""Write a Python program to find the second smallest number in a list."""
def second(list1):
    sorted_list = sorted(list1)
    return sorted_list[1]

my_list = [5,15,8,1,9,4,7]
second_smallest = second(my_list)
print("Second smallest number:", second_smallest)
