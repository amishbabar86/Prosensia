def safe_division(numerator, denominator, precision):
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return round(numerator / denominator, precision)


print(safe_division(10, 2, 2))  
