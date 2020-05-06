"""
change_puhleese.py
=====
You're the manager of a tiny boutique that sells Python related gifts and 
knick-knacks (like plush Python stuffed animals, Guido Van Rossum bobble head
dolls, etc. ). Unfortunately, you don't have any paper bills on hand, you only 
have coins! 

To help you calculate change, you reprogram you cash register to print out the 
exact change that's needed, broken down by quarters, dimes, nickels and pennies.

Here's what your program should do:

1. Ask the cashier for information regarding the items purchased. It will 
   assume that everyone buys exactly three items (!?). For every item:
   a. ask for name of the item
   b. ask for the price (assume that users will always enter a number with a 
      decimal point)
   c. ask for quantity (assume that users will always enter a whole number)
2. Ask the cashier for how much the user paid. Assume that the amount paid
   is at least as much as the total owed (including sales tax)
3. Print out a receipt that contains the following information:
   a. name, price, quantity and total cost per item purchased
   b. the total cost of all of the items
   c. the sales tax based on the cost of all of the items - sales tax in the
      city is 8.875%
   d. the total amount owed, including sales tax
   e. the total amount paid
   f. the change owed, followed by a break down of how many quarters, dimes, 
      nickels and pennies will be given back
      * it will always print out the number of coins for each denomination, 
        even if the quantity is 0
   g. __IT IS OK IF SOME OF YOUR CALCULATIONS ARE OFF BY 1 CENT__
4. The receipt should be in the following format:
   a. the width of the receipt is 80 characters long total
   b. it has a center aligned title: PREMIER PYTHON PLAZA RECEIPT
   c. followed by a line created by equal signs that's 80 characters long (===)
      * __DO NOT TYPE OUT__ 80 ='s ... use what we learned about Python types,
        operators, etc. to do this
   d. print out the costs per item...
   e. print out another line created by equal signs
   f. print out the calculations for total item cost, sales tax, etc.
   g. print out another line created by equal signs
   h. print out the number of quarters, dimes, etc.
   i. "headings" in a line are left justified: item name x quantity ... cost
   j. prices / costs:
      * are right justified
      * have a dollar sign
      * have two decimal places
      * hint: you may have to use format more than once to get the decimal
        places... but then you'll need to add a dollar and format again!
   k. assume that all item names and costs are less than 40 characters long
   l. see the sample interaction below
      * everything after the > (greater than sign) is user input
      * the receipt is at the end
      * __YOUR OUTPUT SHOULD MATCH THE OUTPUT BELOW!__
5. __COMMENT YOUR SOURCE CODE__ by 
   a. briefly describing sections of your program (for example "# calculates the number of quarters, dimes, nickels and pennies" could go above the part of your code that runs those calculations). 
   b. include your name, the date, and your class section at top of your file (above everything else)

What is the name of the first item?
> Guido Van Rossum Bobble Head
How much does the first item cost?
> 10
How many are being purchased?
> 3
What is the name of the second item?
> Python Stuffed Animal
How much does the second item cost?
> 29.99
How many are being purchased?
> 1
What is the name of the third item?
> Hello World T-Shirt
How much does the third item cost?
> 12.50
How many are being purchased?
> 3
How much was paid?
> 150.03
....
                          PREMIER PYTHON PLAZA RECEIPT
================================================================================
3 x Guido Van Rossum Bobble Head                                          $30.00
1 x Python Stuffed Animal                                                 $29.99
3 x Hello World T-Shirt                                                   $37.50
================================================================================
TOTAL COST OF ITEMS                                                       $97.49
SALES TAX                                                                  $8.65
AMOUNT OWED                                                              $106.14
AMOUNT PAID                                                              $150.03
CHANGE                                                                    $43.89
================================================================================
CHANGE:
175 x quarters
1 x dimes
0 x nickels
4 x pennies
"""

# User input for items
item_1 = input("What is the name of the first item?\n>")
C_item_1 = float(input("How much does the first item cost?\n>")) #Converting String to Float
Q_item_1 = int(input("How many are being purchased?\n>")) # Converting String to Integer

# Calculate Item 1 total cost
t_cost_1 = format(C_item_1 * Q_item_1, '.2f')

item_2 = input("What is the name of the second item?\n>")
C_item_2 = float(input("How much does the cost item cost?\n>"))
Q_item_2 = int(input("How many are being purchased?\n>")) # Converting String to Integer

# Calculate Item 2 total cost
t_cost_2 = format(C_item_2 * Q_item_2, '.2f')

item_3 = input("What is the name of the third item?\n>")
C_item_3 = float(input("How much does the third item cost?\n>")) #Converting String to Float
Q_item_3 = int(input("How many are being purchased?\n>")) # Converting String to Integer

# Calculate Item 3 total cost
t_cost_3 = format(C_item_3 * Q_item_3, '.2f')

# Calculate total cost of all 3 items
T_cost = format(float(t_cost_1) + float(t_cost_2) + float(t_cost_3), '.2f')

#City Tax
tax = .08875

#Calculating Tax owed
owed_tax = format(float(T_cost) * tax, '.2f')

# Total cost owed
owed = format((float(T_cost) * tax) + float(T_cost), '.2f')

# Amount paid by user
paid = format(float(input("How much was paid?\n>")), '.2f')

#THe change given to the user
change = format(float(paid) - float(owed), '.2f')

#Converting change to a float
change_2 = float(change)

## Calculating Change

# Setting variables for change
quarter = .25

quarters = 0

dime = .1

dimes = 0

nickel = .05

nickels = 0

penny = .01

pennies = 0


# Calculating Change
if change_2 >= .25:
    quarters = change_2 / quarter
    change_2 = change_2 % quarter
if change_2 >= .1:
    dimes = change_2 / dime
    change_2 = change_2 % .1
if change_2 >= .05:
    nickels = change_2 / nickel
    change_2 = change_2 % nickel
if change_2 >= .01:
    pennies = change_2 / penny

#Converting Change quantities back to integers to get whole numbers
quarters = int(quarters)
dimes = int(dimes)
nickels = int(nickels)
pennies = int(pennies)

# Print Heading
print(format("PREMIER PYTHON PLAZA RECEIPT", '^80'))

# Print Seperator
print("=" * 80) #format(,'80', sep='=')


# Print itemized list
print(format(str(Q_item_1)+ " X " + item_1, '<60'), format( '$' + str(t_cost_1), '>19'))

print(format(str(Q_item_2)+ " X " + item_2, '<60'), format('$' + str(t_cost_2), '>19'))

print(format(str(Q_item_3)+ " X " + item_3, '<60'), format('$' + str(t_cost_3), '>19'))

# Print seperator
print("=" * 80)

# Print Cost Breakdown
print(format('TOTAL COST OF ITEMS', '<60'), format('$' + str(T_cost), '>19'))

print(format('SALES TAX', '<60'), format('$' + str(owed_tax), '>19'))

print(format('AMOUNT OWED', '<60'), format('$' + str(owed), '>19'))

print(format('AMOUNT PAID', '<60'), format('$' + str(paid), '>19'))

print(format('CHANGE', '<60'), format('$' + str(change), '>19'))

#Print seperator
print("=" * 80) #format(,'80', sep='=')

#Print change quantities
print(format('CHANGE:', '<80'))

print(format(str(quarters) + " X quarters", '<80'))

print(format(str(dimes) + " X dimes", '<80'))

print(format(str(nickels) + " X nickels", '<80'))

print(format(str(pennies) + " X pennies", '<80'))

