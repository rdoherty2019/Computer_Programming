def horizontal_line(char : str, width : int, left_padding : int):
    spaces = left_padding * ' '
    text = char * width
    return f'{spaces}{text}'


"""
Build a string and build it character by character
"""
"""
def horizontal_line(str = char, width, left_padding):
    s = ''
    for column_num in range(width):
        s+= chr()
    return f'{leff_padding * " "}{s}'
"""
#print vs return on the effect of other module

#does not return any value. Just prints it
"""def print_equals(char):
    top = horizontal_line(ch, 5, 0)
    bottom = horizontal_line(ch, 5, 0)
    print(top)
    print()
    print(bottom)
"""
"""if __name__ == '__main__':
    res = horizontal_line("x", 3, 2)
    print(res)
"""
#HW Vertical lines nested loops

def vertical_lines(char : str, h : int, left_padding : int,  number : int, interior_offset : int):
    s = ''
    for row_num in range(h):
        r = ''
        for col_num in range(number):
            r += f'{char}{interior_offset * " "}'
        s += f'{left_padding * " "}{r}'
        if row_num < h -1:
            s += '\n'
    return s
"""
print(vertical_lines('*', h = 4, left_padding= 0, number = 2, interior_offset=1))

print("* *\n* *\n* *\n* *")
"""

def vertical_line(char : str, height : int, left_padding : int):
    return vertical_lines(char = char, h = height, left_padding= left_padding,number=1, interior_offset= 0)
'''
print("hortizontal line test")
print(horizontal_line('*', 5, 0))
print()

print("Vertical line test")
vertical_line('*', 2, 5)
print()

print("Vertical Lines test")
print(vertical_lines('+', 4, 0, 5, 3))
print()
'''

def print_zero(char :str, width: int):
    #Setting a floor for the width
    if width < 3:
        width = 3
    #top
    print(horizontal_line(char=char, width=width, left_padding=0))
    #middle
    print(vertical_lines(char = char, left_padding= 0, h = 3, number= 2, interior_offset= width - 2))
    #bottom
    print(horizontal_line(char=char, width=width, left_padding=0))

def print_one(char : str, width : int):
    if width < 3:
        width = 3
    #right formatted
    print(vertical_line(char, 5, width - 1))

def print_two(char: str, width : int):
    if width < 3:
        width = 3
    #top
    print(horizontal_line(char=char, width= width, left_padding= 0))

    #right pad
    print(vertical_line(char=char, height= 1 , left_padding= width -1))

    #middle
    print(horizontal_line(char=char, width= width, left_padding=0))

    #left pad
    print(vertical_line(char= char, height=1, left_padding= 0))

    #bottom
    print(horizontal_line(char=char, width=width, left_padding=0))

def print_three(char : str , width : int):
    if width < 3:
        width = 3
#top
    print(horizontal_line(char=char, width= width, left_padding= 0))
#right format
    print(vertical_line(char=char, height= 1 , left_padding= width -1))

    #middle
    print(horizontal_line(char=char, width= width, left_padding=0))
#right format
    print(vertical_line(char= char, height=1, left_padding= width -1))

    #bottom
    print(horizontal_line(char=char, width=width, left_padding=0))

def print_four(char : str, width : int):
    if width < 3:
        width = 3
    #Top two lines
    print(vertical_lines(char = char, left_padding= 0, h = 2, number= 2, interior_offset= width - 2))

    #Middle
    print(horizontal_line(char= char, width= width, left_padding= 0))

    #bottom
    print(vertical_line(char=char, height= 2, left_padding= width-1))

def print_five(char : str , width : int):
    if width < 3:
        width = 3
    # top
    print(horizontal_line(char=char, width=width, left_padding=0))
#left format
    print(vertical_line(char=char, height=1, left_padding=0))

    # middle
    print(horizontal_line(char=char, width=width, left_padding=0))
#right format
    print(vertical_line(char=char, height=1, left_padding=width -1))

    # bottom
    print(horizontal_line(char=char, width=width, left_padding=0))

def print_six(char : str, width: int):
    if width < 3:
        width = 3
    # top
    print(horizontal_line(char=char, width=width, left_padding=0))
#left format
    print(vertical_line(char=char, height=1, left_padding=0))

    # middle
    print(horizontal_line(char=char, width=width, left_padding=0))

    print(vertical_lines(char=char, h=1, number= 2, interior_offset= width - 2, left_padding=0))

    # bottom
    print(horizontal_line(char=char, width=width, left_padding=0))

def print_seven(char: str, width : int):
    if width < 3:
        width = 3
    # top
    print(horizontal_line(char=char, width=width, left_padding=0))
#right formatted
    print(vertical_line(char=char, height=4, left_padding=width -1))

def print_eight(char : str, width: int):
    if width < 3:
        width = 3
    # top
    print(horizontal_line(char=char, width=width, left_padding=0))

    print(vertical_lines(char=char, h=1, number=2, interior_offset=width - 2, left_padding=0))

    # middle
    print(horizontal_line(char=char, width=width, left_padding=0))

    print(vertical_lines(char=char, h=1, number= 2, interior_offset= width - 2, left_padding=0))

    # bottom
    print(horizontal_line(char=char, width=width, left_padding=0))

def print_nine(char : str, width: int):
    if width < 3:
        width = 3
    # top
    print(horizontal_line(char=char, width=width, left_padding=0))

    print(vertical_lines(char=char, h=1, number=2, interior_offset=width - 2, left_padding=0))

    # middle
    print(horizontal_line(char=char, width=width, left_padding=0))
#right format
    print(vertical_line(char= char, height= 2, left_padding= width -1))

def print_plus(char: str, width : int):
    if width < 3:
        width = 3
    #top
    print(vertical_line(char= char, height = 2, left_padding= width//2))
    #middle
    print(horizontal_line(char=char, width=width, left_padding=0))
    #bottom
    print(vertical_line(char=char, height = 2, left_padding=width // 2))

def print_minus(char: str, width : int):
    if width < 3:
        width = 3
    print()
    print()
    # middle
    print(horizontal_line(char=char, width=width, left_padding=0))
    print()
    print()

def print_multiplication(char: str, width : int):
    if width < 3:
        width = 3
    print(vertical_lines(char=char, h=1, number=2, interior_offset = width - 2, left_padding=0))
    print(vertical_line(char=char, height = 1, left_padding=(width // 2) - 1) + vertical_line(char=char, height = 1, left_padding=1))
    print(vertical_line(char=char, height=1, left_padding=width // 2))
    print(vertical_line(char=char, height = 1, left_padding=(width // 2) - 1) + vertical_line(char=char, height = 1, left_padding=1))
    print(vertical_lines(char=char, h=1, number=2, interior_offset=width - 2, left_padding=0))

def check_answer(left_operand : int, right_operand : int, answer : int, operator : str):
    #plus operator
    if operator == '+':
        test = left_operand + right_operand

        if test == answer:
            return True
        else :
            return False
    #minus operator
    elif operator == '-':
        test = left_operand - right_operand
        if test == answer:
            return True
        else:
            return False
    # multiplication operator
    elif operator == 'X' or operator == '*':
        test = left_operand * right_operand
        if test == answer:
            return True
        else:
            return False
    #default to plus
    else:
        test = left_operand + right_operand
        if test == answer:
            return True
        else:
            return False

'''
print("print 1 test")
print_one('*', 8)
print()

print("Testing zero")
print_zero('*', 8)
print()

print("Testing 2")
print_two('*', 8)
print()

print("Testing 3")
print_three('*', 8)
print()

print("Testing 4")
print_four('*', 8)
print()

print("Testing 5")
print_five('*', 8)
print()

print("testing 6")
print_six('*', 8)
print()

print("Testing 7")
print_seven('*', 8)
print()

print("Testing 8")
print_eight('*', 8)
print()

print("Testing 9")
print_nine('*', 8)
print()

print('Testing Plus')
print_plus('*', 8)
print()

print("Testing Minus")
print_minus('*', 8)
print()

print_multiplication('*', 9)

answer1 = check_answer(1, 2, 3, "+")
print(answer1)
answer2 = check_answer(1, 2, -1, "-")
print(answer2)
answer3 = check_answer(9, 5, 3, "+")
print(answer3)
answer4 = check_answer(8, 2, 4, "-")
print(answer4)
answer3 = check_answer(9, 5, 3, "*")
print(answer3)
'''


