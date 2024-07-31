def string_to_int_with_fallback(input_str, default_value):
    try:
        return int(input_str)
    except ValueError:
        return default_value


print(string_to_int_with_fallback("123", 0))  
print(string_to_int_with_fallback("abc", 0))  
