# Count the number of lines in data.txt
line_count = 0
with open('data.txt', 'r') as file:
    for line in file:
        line_count += 1
print(f"Number of lines in data.txt: {line_count}")
