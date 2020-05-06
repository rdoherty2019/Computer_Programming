"""
lousy_plasma.py
=====
See instructions on course site.
"""

"""
read some lyrics from a file
replace words from those lyrics using synonyms
loaded from another file called theysarus
format of file:

word1, syn1, syn2
word2, syn1
word3, syn1,syn2,syn3
"""

import random
thesaurus = {
    "happy": "glad",
    "sad"  : "bleak"
}


#part0
def remove_punc(s):
    clean_s = ''
    for ch in s:
        if ch.isalpha() or ch == ' ' or ch == "\n":
            clean_s = clean_s + ch

    return clean_s


"""
#user entry
phrase = input("Enter a phrase\n>")
#break into list
words = remove_punc(phrase).split(" ")

#iterate through list
new_words = []
for word in words:
    if word.lower() in thesaurus:
        sub_word = thesaurus[word.lower()]
        
        new_words.append(sub_word.upper())
    else:
        new_words.append(word)
print(" ".join(new_words))



#part1
thesaurus = {
    "happy":["glad",  "blissful", "ecstatic", "at ease"],
    "sad":["bleak", "blue", "depressed"]
}
# user entry
phrase = input("Enter a phrase\n>")
# break into list
words = remove_punc(phrase).split(" ")

# iterate through list
new_words = []
for word in words:
    if word.lower() in thesaurus:
        sub_word = thesaurus[word.lower()]
        values = len(sub_word)
        val_select = random.randint(0,values-1)
        new_words.append(sub_word[val_select].upper())
    else:
        new_words.append(word)
print(" ".join(new_words))
"""

#part2

fr = open('thesaurus.txt', 'r')
thesaurus = {}
for line in fr:
    temp_list = line.split(',')
    thesaurus[temp_list[0]] = [word.strip() for word in temp_list if word.strip() != temp_list[0].strip()]


#part3
fr = open('lousy_plasma.txt', 'r')
#read in whole string
bad_blood = fr.read()
#get formatt correct
words = remove_punc(bad_blood).split(" ")
# iterate through list
new_words = []
for word in words:
    #make sure user entry is same as thes
    if word.lower() in thesaurus:
        #only take half words
        chance = random.randint(1,2)
        # add new word
        if chance == 1:
            sub_word = thesaurus[word.lower()]

            values = len(sub_word)
            val_select = random.randint(0,values-1)
            new_words.append(sub_word[val_select].upper())
        #add existing word
        else:
            new_words.append(word)
    #not a word in thesaurus
    else:
        new_words.append(word)
# join our lyrics
lyrics = " ".join(new_words)

print(lyrics)

# lyrics is the variable that contains the new lyrics to your song
from os import system
system("say -i -v Fiona " + "\"" + lyrics + "\"")