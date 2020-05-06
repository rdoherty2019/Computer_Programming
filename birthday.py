'''
Richie Doherty
'''

import mydate
import listutils
#user input
trials = int(input("How many times should I run the simulation? \n>"))

bdays = int(input("How many birthdays should I generate per trial?\n>"))

#accumulators
trial = 1
counter = 0

#simulation
for it in range(trials):
    #accumulator
    lst = []

    # random birthday creation
    for i in range(bdays):
        lst.append(mydate.generate_date(0,2020))
    #removing years
    lst = mydate.remove_years(lst)

    #if there are duplicate birthdays
    if listutils.has_duplicates(lst) == True:
        #add one to counter
        counter += 1

        #create a list of birthdays
        dupilcate = listutils.get_duplicates(lst)

        #start string
        dupilcates ="("

        #type of string return varys depending on the amount of duplicates
        if len(dupilcate) > 1:
            #add to string
            for d in range(len(dupilcate)):
                #last iteration in duplicates
                if d + 1 == len(dupilcate):
                    #changing number of months to named month
                    dupilcates = dupilcates + mydate.month_num_to_string(dupilcate[d][0]) + ' ' + str(dupilcate[d][1]) + ')'
                else:
                    dupilcates = dupilcates + mydate.month_num_to_string(dupilcate[d][0]) + ' ' + str(dupilcate[d][1]) + ', '
            print("Trail #" + str(trial) + ": " + str(len(dupilcate)) + " dates occur more than once! " + dupilcates)
        elif len(dupilcate) == 1:
            dupilcates = dupilcates + mydate.month_num_to_string(dupilcate[0][0]) + ' ' + str(dupilcate[0][1]) + ')'
            print("Trail #" + str(trial) + ": 1 date occurs more than once! " + dupilcates)

    #no duplicates
    else:
        print("Trail #" + str(trial) + ": No dates are the same.")
    trial += 1

#results output

prob = counter/trials

print("""Results:
=====""")
print("Out of " + str(trials) + " trails, " + str(counter) + " had dates that were repeated.")
print("We can conclude that you have a " + "{:.2%}".format(prob) + " chance of sharing")
print("a birthday with someone if you are in a group of " + str(bdays) + " people")