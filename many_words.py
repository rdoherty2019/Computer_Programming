#assking for input
num = int(input("How many words? \n>"))

#setting empty list to accumulate
s = ''

#iterating through number of words
for i in range(num):
    #reverse order words
    #adds accumlated string to the end of the new word inputed word
    s = input("Word please! \n>") + ' ' + s

print(s)
