def strings_to_ints_with_logging(strings):
    ints = []
    errors = []
    for s in strings:
        try:
            ints.append(int(s))
        except ValueError as e:
            errors.append(f"Error converting '{s}': {str(e)}")
    return ints, errors


strings = ["1", "2", "three", "4", "five"]
ints, errors = strings_to_ints_with_logging(strings)
print(ints)   
print(errors) 
