"""Write a Python function to check whether a number is perfect or not."""
def is_perfect(num):
    if num <= 0:
        return False
    
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    
    return divisor_sum == num
number = 28
print("is a perfect number: ",is_perfect(number))
