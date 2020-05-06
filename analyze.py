def is_odd(x):
    #Module will leave a remainder if it is not divisable
    num = x % 2
    if num != 0:
        return True
    else:
        return False


def is_prime(x):
    for i in range(1, x+1):
        if i == x or i == 1:
            continue
        num = x % i
        if num == 0:
            return False
    return True



def is_abundant(x):
    acc = 0
    for i in range(1, x+1):
        if i == x:
            continue
        num = x % i
        if num == 0:
            acc+= i
    if acc > x:
        return True
    else:
        return False

user = int(input("Please enter a number: \n>"))

if is_odd(user) == True:
    print(str(user) + " is odd")
else:
    print(str(user) + " is not odd")

if is_prime(user) == True:
    print(str(user) + " is prime")
else:
    print(str(user) + " is not prime")
if is_abundant(user) == True:
    print(str(user) + ' is abundant')
else:
    print(str(user) + ' is not abundant')


