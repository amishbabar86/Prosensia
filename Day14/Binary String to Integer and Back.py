def binary_conversion(binary_str, fixed_length=8):
    try:
        integer_value = int(binary_str, 2)
        binary_string = format(integer_value, '0' + str(fixed_length) + 'b')
        return binary_string
    except ValueError as e:
        return f"Error: {e}"


result = binary_conversion("1010")
print(result)  
