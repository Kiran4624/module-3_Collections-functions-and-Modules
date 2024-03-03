"""Write a Python function to check whether a number is in a given range"""
def in_range(num, start, end):
    return start <= num <= end


num = 5
start_range = 1
end_range = 10
print(f"{num} is in the range [{start_range}, {end_range}]: {in_range(num, start_range, end_range)}")
