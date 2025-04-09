# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# count_word_frequency(words)
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}


def count_word_frequency(words):
    wordFrequency = {}

    for word in words:
        if word not in wordFrequency.keys():
            wordFrequency.setdefault(word, 0)

        wordFrequency[word] += 1

    return wordFrequency
