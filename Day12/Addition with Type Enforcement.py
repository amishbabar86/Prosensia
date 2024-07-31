def add_with_type_enforcement(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a + b


print(add_with_type_enforcement(1, 2))       
# print(add_with_type_enforcement(1, "two"))  
