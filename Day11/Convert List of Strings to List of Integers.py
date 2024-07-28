def list_of_strings_to_integers(lst):
    result = []
    for s in lst:
        try:
            result.append(int(s))
        except ValueError:
            continue
    return result


print(list_of_strings_to_integers(["123", "abc", "456"]))  
