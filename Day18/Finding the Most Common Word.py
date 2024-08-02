# Finding the most common word in a file
def most_common_word(filename):
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()  # Make case-insensitive
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    max_word = max(word_count, key=word_count.get)
    return max_word, word_count[max_word]


filename = 'textfile.txt'
word, count = most_common_word(filename)
print(f"The most common word is '{word}' with {count} occurrences.")
