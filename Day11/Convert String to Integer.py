def string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return None


print(string_to_integer("123"))  
print(string_to_integer("abc"))  
