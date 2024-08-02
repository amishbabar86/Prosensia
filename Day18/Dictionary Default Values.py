# Using get method to retrieve a value and return a default value if the key doesn't exist
my_dict = {'key1': 'value1', 'key2': 'value2'}
key = 'key3'
value = my_dict.get(key, 0)
print(f"The value for '{key}' is {value}")
