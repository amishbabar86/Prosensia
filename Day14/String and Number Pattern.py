import re

def matches_pattern(string, pattern):
    regex_pattern = ''
    for char in pattern:
        if char.isalpha():
            regex_pattern += '[a-zA-Z]'
        elif char.isdigit():
            regex_pattern += '[0-9]'
        else:
            regex_pattern += re.escape(char)
    
    return bool(re.fullmatch(regex_pattern, string))


result = matches_pattern("a1b2", "a1b2")
print(result) 
