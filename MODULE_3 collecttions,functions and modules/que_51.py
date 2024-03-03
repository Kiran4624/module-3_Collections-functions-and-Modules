"""Write a Python function that checks whether a passed string is 
palindrome or not """
def is_palindrome(string):
  
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

test_string = "A man, a plan, a canal, Panama!"
print( "is a palindrome: ",is_palindrome(test_string))
