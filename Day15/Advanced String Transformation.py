def transform_string(s):
    def digit_to_word(digit):
        return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][int(digit)]
    
    words = s.split()
    transformed_words = []
    for word in words:
        transformed_word = ''.join(digit_to_word(c) if c.isdigit() else c for c in word)
        if len(transformed_word) > 5:
            transformed_word = transformed_word[::-1]
        transformed_words.append(transformed_word)
    
    return ' '.join(transformed_words).title()

def main():
    s = "Hello 123 world 456789"
    print("Transformed string:", transform_string(s))

main()
