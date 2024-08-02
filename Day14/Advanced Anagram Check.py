import re
from collections import Counter

def are_anagrams(str1, str2):
    cleaned_str1 = re.sub(r'[^a-zA-Z0-9]', '', str1).lower()
    cleaned_str2 = re.sub(r'[^a-zA-Z0-9]', '', str2).lower()

    if Counter(cleaned_str1) == Counter(cleaned_str2):
        return True, Counter(cleaned_str1), Counter(cleaned_str2)
    else:
        return False, Counter(cleaned_str1), Counter(cleaned_str2)


result = are_anagrams("Astronomer", "Moon starer!")
print(result)  
