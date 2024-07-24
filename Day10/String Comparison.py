def compare_strings(str1, str2):
    if str1 < str2:
        return f"{str1} comes before {str2}"
    elif str1 > str2:
        return f"{str1} comes after {str2}"
    else:
        return f"{str1} is equal to {str2}"


print(compare_strings("apple", "banana"))  # Output: apple comes before banana
print(compare_strings("cherry", "banana"))  # Output: cherry comes after banana
print(compare_strings("date", "date"))  # Output: date is equal to date
