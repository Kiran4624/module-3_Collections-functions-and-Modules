"""Write a Python program to find the repeated items of a tuple"""


my_tuple = (1, 2, 3, 4, 2, 3, 5, 6, 5)
my_list=[]
for i in my_tuple:
    if my_tuple.count(i)>1:
        if i not in my_list:
            my_list.append(i)
print(my_list)
