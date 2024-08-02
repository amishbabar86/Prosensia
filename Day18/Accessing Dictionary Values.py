# Function to print the value associated with a specified key
def print_value(dictionary, key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print("Key not found")

# Example usage
my_dict = {'key1': 'value1', 'key2': 'value2'}
print_value(my_dict, 'key1')  # Outputs: value1
print_value(my_dict, 'key3')  # Outputs: Key not found
