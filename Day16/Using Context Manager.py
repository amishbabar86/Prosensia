# Read data.txt using a context manager (with statement)
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
