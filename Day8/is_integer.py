def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Testing the function with "123" and "hello"
print(is_integer("123"))
print(is_integer("hello"))
