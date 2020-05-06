"""
Richie Doherty
"""

import random

#generating number of words
num_words = random.randint(3,6)

print("I'll need " + str(num_words) + " words")

#starting list to hold inputs
words = []

#Asking for N number of inputs
for i in range(num_words):
    words.append(input("Word " + str(i + 1) + " please! \n>"))

#Setting variables
word_length = []

#Setting the benchmarking for longest and shortest word
longest_word = ''
shortest_word = words[0]

#Iterating through every word in the list
for w in words:
    if len(w) > len(longest_word):
        longest_word = w
    if len(w) < len(shortest_word):
        shortest_word = w
    word_length.append(len(w))

#Printing Results
print("The largest word: " + str(longest_word) )
print("The shortest word: " + str(shortest_word) )
print("The average length of the entered words: " + str(sum(word_length)/len(word_length)))
