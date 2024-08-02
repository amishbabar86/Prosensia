# Handling KeyError exception by printing a custom error message
my_dict = {'key1': 'value1', 'key2': 'value2'}

try:
    print(my_dict['key3'])
except KeyError:
    print("Custom Error: The key 'key3' does not exist in the dictionary.")
