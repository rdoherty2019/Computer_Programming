#setting condtion
num = 0

#infinite loop until user changes the condition
#keeps asking for input
while num < 1 :
    num = int(input("Enter height of your pyramid"))



#add rows

triangle = ''

#setting length of format
space = len(str(num))

#Rows
for row_num in range(num):
    #start accumulator for row
    r = ''
    #column
    for column in range(-num, num+1):
        #Skipping duplicate number
        if column == -1:
            continue
        #we don't want zero is our pyramind
        if column == 0:
            continue
        #resetting space for each loop
        space = len(str(num))

        #built criteria setter
        value = abs(column)

        #accounting for change in number character ammount
        if space == len(str(value)):
            space += 1

        # replacing number with space to give pyramind shape
        if value > row_num + 1:
            r += str(' ' * space) # add two spaces for the space and the value itself
        #adding number to string
        else:
            r += format(value, str(space))

    #adding row to bottom of pryamid
    triangle += r + "\n"

#printing result after loop
print(triangle)
