# Function to merge two dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

# Example usage
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {'key2': 'updated_value2', 'key3': 'value3'}
result = merge_dicts(dict1, dict2)
print(result)
