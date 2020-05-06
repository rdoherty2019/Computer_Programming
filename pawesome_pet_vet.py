'''
Richie Doherty
pawesome_pet_vet.py
'''

import animal_functions
import practice
def main():
    checked_in = [['edgrr allan', 'dog' ,80 ],['jane clawston','cat',20] ,['franze catka','cat ',60], ['bark twain', 'dog', 40]]
    t1 = False
    while t1 == False:
        menu = input("check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit \n>")
        if menu == 'q':
            t1 = True
        elif menu.lower() == 'i':
            name = input("What is the pet's name?\n>")
            kind = input("What kind of animal is the pet?\n>")
            urgent = int(input("How urgently does the pet need help (0-100)?\n>"))
            while urgent > 100 or urgent < 0:
                urgent = int(input("Please enter (0-100)\n>"))
            checked_in.append([name,kind,urgent])
            print(name + " is checked in.")
        elif menu.lower() == 'o':
            print(animal_functions.stringify_animals(checked_in))
            check_out = int(input("Please enter a number to check an animal out of the clinic\n>"))
            checked_out = checked_in.pop(check_out-1)
            print(animal_functions.stringify_animals(checked_in))
            print(checked_out[0] + ' is checked out')
        elif menu.lower() == 'a':
            display = animal_functions.sort_by_name(checked_in)
            print(animal_functions.stringify_animals(display))
        elif menu.lower() == 'm':
            display = animal_functions.get_most_urgent(checked_in)
            print(display[0] + ', ' + display[1] + ' with urgency ' + str(display[2]) + ', should be seen right away!')
        elif menu.lower() == 'l':
            display = sorted(checked_in, key= lambda animal : animal[2])
            print(display[0][0] + ', ' + display[0][1] + ' with urgency ' + str(display[0][2]) + ', can wait!')
        elif menu.lower() == 'f':
            name = input("Please enter a name to search for \n>")
            print(animal_functions.find_by_name(name,checked_in))

main()

