# Handle the case when data.txt does not exist and print a user-friendly error message
try:
    with open('data.txt', 'r') as file:
        pass
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist.")
