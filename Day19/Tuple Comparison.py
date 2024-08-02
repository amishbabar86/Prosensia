def compare_tuples(t1, t2):
    return [a == b for a, b in zip(t1, t2)]

# Compare two tuples
t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(compare_tuples(t1, t2))  
