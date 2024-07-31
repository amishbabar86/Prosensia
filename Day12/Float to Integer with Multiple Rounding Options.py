import math

def float_to_int_with_rounding(value, strategy):
    if strategy == "up":
        return math.ceil(value)
    elif strategy == "down":
        return math.floor(value)
    elif strategy == "nearest":
        return round(value)
    else:
        raise ValueError("Invalid rounding strategy")


print(float_to_int_with_rounding(3.7, "up"))       
print(float_to_int_with_rounding(3.7, "down"))     
print(float_to_int_with_rounding(3.7, "nearest"))  
