def reverse_and_sort_dict(d):
    return sorted([(value, key) for key, value in d.items()])

# Create a dictionary
my_dict = {'a': 10, 'b': 1, 'c': 22}
# Reverse and sort
print(reverse_and_sort_dict(my_dict))  
