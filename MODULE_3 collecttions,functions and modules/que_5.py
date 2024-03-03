"""How will you compare two lists?"""

def compare(l1,l2):
    l1.sort()
    l2.sort()
    if(l1==l2):
        return "Equal"
    else:
        return "Not Equal"

list1=[4,28,24]
list2=[28,20,4]
print("comparision is :",compare(list1,list2))



