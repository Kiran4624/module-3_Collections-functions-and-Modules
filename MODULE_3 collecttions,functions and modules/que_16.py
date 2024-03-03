"""Write a Python program to check whether a list contains a sub list"""
def sub(main_list, sublist):
    if not sublist:
        return True
    
    for i in range(len(main_list)):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False
main_list =[1, 2, 3, 4, 5, 6, 7, 8]
sub1 =[3, 4, 5]
sub2 =[7, 8, 9]

# print("Main list:",main_list)
# print("Sublist 1:",sub1)
# print("Sublist 2:",sub2)

print("Does the main list contain sublist 1?",sub(main_list, sub1))
print("Does the main list contain sublist 2?",sub(main_list, sub2))

