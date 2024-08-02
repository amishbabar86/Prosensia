from collections import Counter

def top_n_words(filename, N):
    with open(filename, 'r') as file:
        words = file.read().lower().split()
        word_counts = Counter(words)
        return word_counts.most_common(N)

# Example usage (assuming you have a file named 'romeo.txt')
# print(top_n_words('romeo.txt', 3))
