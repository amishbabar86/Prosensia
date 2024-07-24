import re

def remove_whitespace(s):
    s = s.strip()
    s = re.sub(r'\s+', ' ', s)
    return s


print(remove_whitespace("  hello   world  "))  
