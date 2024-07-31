def int_to_formatted_string(number, format_spec):
    return format(number, format_spec)


print(int_to_formatted_string(12345, "08d"))  
print(int_to_formatted_string(12345, ".2e"))  
