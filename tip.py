"""
Richie Doherty
"""

#Create Header
print(format('-------', '^40' ))
print(format('/// WELCOME \\\\\\', '^40' ))
print(format('-------', '^40' ))
print(format('Perhaps I can help you calculate $$$ for your tip!', '40' ))

#Ask user for bll and party size
people = int(input("How many people? \n>"))
bill = float(input("How much did it cost? \n>"))

#Set tip percentages
terrible = 0
poor = .1
ok = .15
good = .2
great = .25

#Criteria building for user experience assesment

#parties under 6
if people < 6:

    #User input for user experience
    service = input("How was the service (terrible, poor, ok, good, great)? \n> ")
    if service == 'terrible':
        print("You should probably tip $" + format(bill * terrible, '.2f')+ '!')
    elif service == 'poor':
        print("You should probably tip $" + format(bill * poor, '.2f')+ '!')
    elif service == 'ok':
        print("You should probably tip $" + format(bill * ok, '.2f')+ '!')
    elif service == 'good':
        print("You should probably tip $" + format(bill * good, '.2f')+ '!')
    elif service == 'great':
        print("You should probably tip $" + format(bill * great, '.2f')+ '!')

#invalid user experience entry results in 20% suggestion
    else:
        print("Can't understand entry, "
              "reverting to default tip of 20%, "
              "you should probably tip $" + format(bill * good, '.2f') + '!')

# If party is larger than 5 we tip 20%
else:
    print( "You should probably tip $" + format(bill * good, '.2f') + '!')