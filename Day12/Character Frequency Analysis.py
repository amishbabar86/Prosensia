import re
from collections import Counter

def is_palindrome_with_freq_analysis(input_str):
    cleaned_str = re.sub(r'[^A-Za-z0-9]', '', input_str).lower()
    is_palindrome = cleaned_str == cleaned_str[::-1]
    char_freq = dict(Counter(cleaned_str))
    return is_palindrome, char_freq


input_str = "A man, a plan, a canal, Panama!"
is_palindrome, freq = is_palindrome_with_freq_analysis(input_str)
print(is_palindrome)  
print(freq)           
