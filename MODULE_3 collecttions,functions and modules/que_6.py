"""Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings. """

count = 0
my_list=['kirak','424','abc','viral']
for i in my_list:
    if len(i)>1 and i[0]==i[-1]:
        print("the given words are :",i)
        count += 1
print("number of words you want :",count)