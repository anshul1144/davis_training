# Write a program to count words in sentence.

# Function to count words in a sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)
# Get user input
input_sentence = input("Enter a sentence: ")
result = count_words(input_sentence)

print(f"Number of words: {result}")

""" Output:
Enter a sentence: Python is great
Number of words: 3
"""