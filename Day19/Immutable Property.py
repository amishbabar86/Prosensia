# Create a tuple
fruits = ('apple', 'banana', 'cherry')

try:
    # Attempt to change the second element
    fruits[1] = 'orange'
except TypeError as e:
    print(f"Error: {e}")  
