""" Write a Python program to check a list is empty or not."""

def my_list(list1):
    if not list1:
        return True
    else:
        return False
l1 = ['kiran']

if my_list(l1):
    print("The list is empty.")
else:
    print("The list is not empty.")
