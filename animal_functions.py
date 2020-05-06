'''
Richie Doherty
animal_functions
'''

def find_by_name(name , animals):
    new_list = [animal for animal in animals if name in animal]
    for animal in animals:
        if name in animal:
            return animal
    return None


def stringify_animals(animals):
    s = ''
    its = 1
    for animal in animals:
        s =s + str(its) + " - " + animal[0] + ', ' + animal[1] + "\n"
        its +=1
    return s



def get_most_urgent(animals):
    urgent = [0,0,0]
    for animal in animals:
        if animal[2] >= urgent[2]:
            urgent = animal
    return urgent



def sort_by_name(animals):
    new_list = animals
    for cur in range(len(new_list)):
        min_index = cur
        for search in range(cur + 1, len(new_list)):
            if new_list[search] < new_list[min_index]:
                min_index = search
        if cur != min_index:
            new_list[cur], new_list[min_index] = new_list[min_index], new_list[cur]
    return new_list


if __name__ == '__main__':
    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
    res = find_by_name('sam', animal_list)
    print(res)  # ['sam', 'snake', 4]

    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]

    # returns the string: "1 - sam, snake\n2 - gertrude, goat\n3 - ang, unicorn"
    res = stringify_animals(animal_list)

    print(res)

    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
    print(get_most_urgent(animal_list))

    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
    sorted_animal_list = sort_by_name(animal_list)
    print(sorted_animal_list)
    # will print out [['ang', 'unicorn', 50], ['gertrude', 'goat', 99], ['sam', 'snake', 4]]
    animal_list = [['zim', 'dog', 10], ['bev', 'dog', 10], ['ari', 'cat', 10]]
    sorted_animal_list = sort_by_name(animal_list)
    print(sorted_animal_list)

