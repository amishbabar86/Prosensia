# Find and print all lines that contain the word "error" in log.txt
with open('log.txt', 'r') as file:
    for line in file:
        if 'error' in line:
            print(line, end='')
