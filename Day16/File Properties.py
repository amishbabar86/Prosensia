# Print the size of data.txt in bytes
import os

file_size = os.path.getsize('data.txt')
print(f"Size of data.txt: {file_size} bytes")
