"""
variable_names.py

Richie Doherty

=====
You're tired of inadvertently writing Python variable names that aren't valid,
so you decide to write a program that checks the validity of variable names.

To write this program, you'll create a function called is_valid_name. Your
program will then continually ask the user for a variable name, and you'll use
your function to determine whether or not it's valid. If the user enters an
invalid variable name 3 times in a row or if they enter a valid name, stop
asking for a variable name!

a) Create a function called is_valid_name
   * parameters: a string representing a variable name
   * body: use the rules below to determine whether or not the variable is
     valid
   * return: either true or false depending on whether or not the variable
     name is valid
b) A valid variable name:
   * starts with only an underscore or a letter
   * is only composed of underscores, letters or numbers
c) Within an conditional at the end of your function, write your program...
    if __name__ == '__main__':
        # your program goes here
d) Continually ask the user for a variable names
e) Use your function to check if it's valid
f) If  the user enters a valid name... or if they enter 3 invalid names, stop asking

Example usage of function:
-----
print(is_valid_name('1asdf')) # False
print(is_valid_name('#foo'))  # False
print(is_valid_name('asdf1')) # True
print(is_valid_name('_foo'))  # True
print(is_valid_name('f_oo'))  # True

Example Interaction of program that uses above function:

Variable name plz
> $hello
Variable name plz
> hello
"""
#defining function
def is_valid_name(string):
    #testing first letter
    if string[0].isalpha() or string[0] == '_':
        #iterating through each letter fo string to test
        for i in string:
            #is it a letter
            if i.isalpha():
                continue
            #is it a number
            elif i.isnumeric():
                continue
            #is it an underscore
            elif i == '_':
                continue
            #if its not return a false
            else:
                return False
        #if it goes through the whole string its true
        return True
    #if the first letter is not an underscore or letter return a false
    else:
        return False

if __name__ == '__main__':
    #set test
    test = False
    #set accumulator
    acc = 0
    #infinity loop
    while test == False:
        #user input
        name = input("Variable name plz \n>")
        #If its a valid name end the loop
        if is_valid_name(name) == True:
            test = True
        #if its not valid try again
        else:
            #add to the accumulator
            acc += 1
        #if its been 3 wrong in a wrong end it
        if acc == 3:
            test = True
