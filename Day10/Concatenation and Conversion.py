def concatenate_and_convert(str1, str2):
    result = str1 + str2
    if result.isdigit():
        return int(result)
    return result


print(concatenate_and_convert("123", "456"))