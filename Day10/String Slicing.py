def slice_string(s, start, end):
    start = max(0, start)
    end = min(len(s), end)
    return s[start:end]


print(slice_string("hello", 1, 4))  
print(slice_string("hello", -1, 10))  
