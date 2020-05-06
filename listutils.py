"""
Richie Doherty
"""
def get_duplicates(lst):
    new_list = []
    for i in lst:
        if lst.count(i) > 1:
            if i in new_list:
                continue
            new_list.append(i)
    return new_list

assert get_duplicates([1, 2, 3, 1, 4, 2]) == [1, 2], "Check to make sure there aren't duplicates in the output"
duplicates = get_duplicates([1, 2, 3, 1, 4, 2])


assert get_duplicates([1,2,2,3,4,4,4]) == [2,4], "Check to make sure there aren't duplicates in the output"
duplicates = get_duplicates([1,2,2,3,4,4,4])


def has_duplicates(lst):
    temp = lst[:]
    for i in lst:
        temp.remove(i)
        if i in temp:
            return True
        temp = lst[:]
    return False

assert has_duplicates([1,2,2,3,4,4,4]) == True
assert has_duplicates([1,2,3]) == False

def join_elements_with(glue, lst):
    s = ''
    for i in range(len(lst)):
        s = s + str(lst[i])
        if i != len(lst) - 1:
            s = s + glue
    return s
assert join_elements_with('X', ['cat', 'dog', 'bat']) == 'catXdogXbat', "Check last glue"



def fill(size, fill_value = 0):
    lst = [fill_value]
    lst = lst * size
    return  lst
assert fill(5) == [0, 0, 0, 0, 0], "Check multiplication"
assert fill(3, 'hi') == ['hi', 'hi', 'hi'], "Check Fill Values"

import random

def random_choose(lst):
    num = random.randint(0, len(lst) - 1)
    return lst[num]

weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
assert random_choose(weekdays) in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], "Check Range"


def random_fill(min_val, max_val, list_length):
    lst = []
    for i in range(list_length):
        i = random.randint(min_val, max_val)
        lst.append(i)
    return lst

assert len(random_fill(1, 10, 4)) == 4, 'Check for loop'


def stringify_elements(lst):
    return [str(ele) for ele in lst]

assert stringify_elements([1, 2, 3]) == ['1', '2', '3'] , "should convert to string"



def mean(lst):
    num = 0
    for i in range(len(lst)):
        num += lst[i]
    num = num / len(lst)
    return num

assert type(mean([1, 2, 3, 4, 5])) == float , 'check type'
assert mean([1, 2, 3, 4, 5]) == 3.0, 'check for loop and divide'
