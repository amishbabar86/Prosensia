def divide_two_numbers(a, b):
    if b == 0:
        return None  # or you can return 'Infinity' or raise an exception
    return a / b


print(divide_two_numbers(10, 5))  
print(divide_two_numbers(10, 0))  
