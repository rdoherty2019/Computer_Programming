import funcynum
import random

test = False

while test == False:
    num_problems = int(input('How many problems? \n>'))
    if num_problems >= 3 and num_problems <= 20:
        test = True
    else:
        print('Please enter a number between 5 and 20.')

test = False

while test == False:
    char = input('What character do you want the numbers to be made of? \n>')
    if len(char) == 1:
        test = True
    else:
        print('Please enter a single character!')


width = int(input('How wide do you want each number to be? \n>'))
if width < 3:
    width = 3
    print('Oops... defaulting to width 3')

correct = 0

for i in range(num_problems):
    left_operand = random.randint(0, 9)
    right_operand = random.randint(0, 9)
    operation = random.randint(1, 3)
    print("What is ...")
    #left operand
    if left_operand == 0:
        funcynum.print_zero(char, width)
    elif left_operand == 1:
        funcynum.print_one(char, width)
    elif left_operand == 2:
        funcynum.print_two(char, width)
    elif left_operand == 3:
        funcynum.print_three(char, width)
    elif left_operand == 4:
        funcynum.print_four(char, width)
    elif left_operand == 5:
        funcynum.print_five(char, width)
    elif left_operand == 6:
        funcynum.print_six(char, width)
    elif left_operand == 7:
        funcynum.print_seven(char, width)
    elif left_operand == 8:
        funcynum.print_eight(char, width)
    elif left_operand == 9:
        funcynum.print_nine(char, width)

    #operation
    if operation == 1:
        operation = '+'
        funcynum.print_plus(char, width)
    elif operation == 2:
        operation = '-'
        funcynum.print_minus(char, width)
    elif operation == 3:
        operation = "*"
        funcynum.print_multiplication(char, width)

    #right operand
    if right_operand == 0:
        funcynum.print_zero(char, width)
    elif right_operand == 1:
        funcynum.print_one(char, width)
    elif right_operand == 2:
        funcynum.print_two(char, width)
    elif right_operand == 3:
        funcynum.print_three(char, width)
    elif right_operand == 4:
        funcynum.print_four(char, width)
    elif right_operand == 5:
        funcynum.print_five(char, width)
    elif right_operand == 6:
        funcynum.print_six(char, width)
    elif right_operand == 7:
        funcynum.print_seven(char, width)
    elif right_operand == 8:
        funcynum.print_eight(char, width)
    elif right_operand == 9:
        funcynum.print_nine(char, width)

    answer = int(input("= "))

    cor_ans = funcynum.check_answer(left_operand, right_operand, answer, operator = operation)

    if cor_ans == True:
        print('Correct!')
        correct += 1
    else:
        print("Nope, the answer is " + str(answer))
percent = (correct / num_problems) * 100

print("You got "  + format(percent, '.2f') + '% correct ' + str(correct) + ' out of ' + str(num_problems))
