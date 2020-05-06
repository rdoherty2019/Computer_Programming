'''
Richie Doherty
'''

import listutils
import random
def is_valid_month_num(n):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    if n in months:
        return True
    else:
        return False
assert is_valid_month_num(3) == True

assert is_valid_month_num(37) == False


def month_num_to_string(month_num):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if is_valid_month_num(month_num) == True:
        return months[month_num - 1]
    else:
        return None
assert month_num_to_string(1) == 'January'

assert month_num_to_string(10) == 'October'

assert month_num_to_string(234) == None


def date_to_string(date_list):
    s = ''
    s = s + month_num_to_string(date_list[1])
    date_list = listutils.stringify_elements(date_list)
    return s + ' ' + date_list[-1] + ', ' + date_list[0]
assert date_to_string([1979, 10, 7]) == 'October 7, 1979'


def dates_to_strings(list_of_date_lists):
    lst = []
    for i in range(len(list_of_date_lists)):
        lst.append(date_to_string(list_of_date_lists[i]))
    return lst
assert dates_to_strings([[1979, 10, 7], [2000, 2, 20]]) == ['October 7, 1979', 'February 20, 2000']

def remove_years(list_of_date_lists):
    for i in range(len(list_of_date_lists)):
        list_of_date_lists[i] = list_of_date_lists[i][1:]
    return list_of_date_lists
assert remove_years([[1979, 10, 7], [2000, 2, 20]]) == [[10, 7], [2, 20]]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_num_days_in_month(month_num, year):
    days = [30,31,28,29]
    if is_valid_month_num(month_num) == True:
        if month_num in [1,3,5,7,8,10,12]:
            return days[1]
        elif month_num in [4,6,9,11]:
            return days[0]
        elif month_num == 2:
            if is_leap_year(year) == True:
                return days[-1]
            elif is_leap_year(year) == False:
                return days[2]
    else:
        return None
assert get_num_days_in_month(2, 1988) == 29 , "check leap year"
assert get_num_days_in_month(2, 1900) == 28 , "check leap year"
assert get_num_days_in_month(11, 1900) == 30, " check months"
assert get_num_days_in_month(12, 1900) == 31, " check months"
assert get_num_days_in_month(1, 1900) == 31, "check months"
assert get_num_days_in_month(30, 1999) == None, "check validator"

def generate_date(start_year, end_year):
    lst = []
    lst.append(random.randint(start_year,end_year))
    lst.append(listutils.random_choose(list(range(1,13))))
    days = get_num_days_in_month(lst[1],lst[0])
    lst.append(listutils.random_choose(list(range(1, days + 1))))
    return lst
