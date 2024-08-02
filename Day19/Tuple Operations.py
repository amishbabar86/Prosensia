# Create a list and a tuple
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# Append to the list
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

try:
    # Attempt to append to the tuple
    my_tuple.append(4)
except AttributeError as e:
    print(f"Error: {e}")  
