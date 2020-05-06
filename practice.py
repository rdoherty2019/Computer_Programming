"""
Richie Doherty
"""
def flattened(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.extend(lst[i])
    return new_lst


def shift_left(lst, n, fill_value=0):
    l = len(lst)
    shift = n
    index = l - shift
    for i in range(n):
        lst[i] = lst[index]
        lst[index] = fill_value
        index +=1



def shifted_left(lst,n, fill_value=0):
    new_list = []
    l = len(lst)
    shift = n
    index = l - shift
    for i in range(n):
        new_list.append(lst[index])
        index +=1
    for i in range(n):
        new_list.append(fill_value)
    return new_list



def shift_right(lst, n, fill_value=0):
    l = len(lst)
    shift = n
    index = l - shift
    for i in range(n):
        lst[index] = lst[i]
        lst[i] = fill_value
        index += 1




def shifted_right(lst, n, fill_value=0):
    new_list = []
    for i in range(n):
        new_list.append(fill_value)
    for i in range(n):
        new_list.append(lst[i])
    return new_list



def fill_in_place(lst, fill_value=0):
    for i in range(len(lst)):
        lst[i]= fill_value



def truncate_long_words(words,n):
    new_list = [word[0:n] + '...' for word in words if len(word) > n]
    return new_list



def sum_positive_parts(lst):
    new_list = [sum(tupe) for tupe in lst if sum(tupe) >= 0]
    return new_list


def consecutive_chars(start_ch, end_ch):
    if len(start_ch) == 1 and len(end_ch) == 1:
        new_list = [chr(ch) for ch in range(ord(start_ch), ord(end_ch) + 1) if ord(start_ch) < ord(end_ch) ]
        return ''.join(new_list)
    else:
        return ''



def unique(*lsts):
    s = set()
    for nums in lsts:
        nums = set(nums)
        diff = nums.difference(s)
        s = s|diff
    return s


if __name__ == '__main__':
    print("put your test cases here")
    nested = [[1, 2], [3, 4]]
    flat = flattened(nested)
    print(flat)

    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)
    print(numbers)
    numbers = [1, 2, 3, 4]
    nums = shifted_left(numbers, 2)
    print(nums)
    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)
    print(numbers)
    numbers = [1, 2, 3, 4]
    nums = shifted_right(numbers, 2)
    print(nums)
    numbers = [1, 2, 3, 4]
    fill_in_place(numbers)
    print(numbers)
    print(truncate_long_words(['aardvark', 'bison', 'chameleon'], 5))
    print(sum_positive_parts([(1, 2), (3, 4)]))
    print(consecutive_chars('A', 'Z'))
    print(consecutive_chars('x', 'z'))
    print(consecutive_chars('Z', 'Z'))
    print(consecutive_chars('Z', 'A'))
    print(consecutive_chars('AAA', 'Z'))
    print(unique([1, 2, 3], [2, 3, 4], [3, 4, 5]))