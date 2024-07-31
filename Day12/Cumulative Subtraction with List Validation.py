def cumulative_subtraction(numbers):
    if len(numbers) < 2 or not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("List must contain at least two numeric elements")
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result


print(cumulative_subtraction([10, 1, 2, 3]))  
       
