"""
Print out each number
or accumulate  and print out each row
Accumulate into big string
"""

num = 0
while num < 1 :
    num = int(input("Enter height of your pyramid"))


"""
for row_num in range(len(num)):
    for col_num in range(num):
        n = 0
       # while n != num:
           # n += 1
        for i in range(num, 0, -1):
            print(num)
"""

#Height
triangle = ''

#space = len(str(num))

for row in range(num):
    r = ''

    if num > 9 & row < 9:
        r += " "

    if num > 99 & row < 99:
        if num > 99 & row < 9:
            r += "  "

    #if space != len(str(row)):
       # r += ' '
    for i in range(num, 0, -1):
        if i > row + 1:
            r += " " #* len(str(num))
            r += ' '
        else:
            r += format(str(i), str(len(str(num))))
           # r += ' '
            if i >= 10:
                r += ' '
    for i in range(2, num + 1):
        if i > row + 1:
            r += " " #* len(str(num))
            r += ' '
        else:
            r += format(str(i), str(len(str(num))))
            #r += ' '
            if i >= 10:
                r += ' '
    triangle += r + "\n"

"""        
    if num > 10:
        if row + 1 > 10:
            triangle += r + "\n"
        else:
            triangle += ' ' + r + "\n"
    elif num > 100:
        triangle += '  ' + r + "\n"
    else:
        triangle += r + "\n"
    """
#print(triangle)

#base



#removing elements/ replacing elements

"""
for row_num un range(n):
    row = ''
    for colu_num in range(-n, n+1:
        valie = abs(col_num
        if value > row_num + 1:
            row += '  '
        else:
            row += str(value) + " "
    triangle += row + "\n"
    
"""

"""
num = 0
while num < 1 :
    num = int(input("Enter height of your pyramid"))

triangle = ''

for row_num in range(num):
    row = ''
    for column_num in range(-num, num+1):
        if column_num == -1:
            continue
        if column_num == 0:
            continue
        value = abs(column_num)

        if value > row_num + 1:
            row += ' '
        else:
            row += format(str(value), str(len(str(num)))) + ' '

    triangle += row + "\n"
print(triangle)
"""


