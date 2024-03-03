"""  Write a Python function that takes two lists and returns true if they have 
at least one common member"""


def common(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

list1 = [1,2,3,4,5]
list2 = [19,6,7,8,9]
print(common(list1, list2))  




