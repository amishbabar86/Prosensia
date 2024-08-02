# Function to print a list of keys and a list of values from a dictionary
def print_keys_values(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    print("Keys:", keys)
    print("Values:", values)

# Example usage
my_dict = {'key1': 'value1', 'key2': 'value2'}
print_keys_values(my_dict)
