def get_char_at_index(s, index):
    try:
        return s[index]
    except IndexError:
        return "Index out of bounds"


print(get_char_at_index("hello", 1))