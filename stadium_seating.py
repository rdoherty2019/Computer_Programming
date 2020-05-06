"""
stadium_seating.py
=====
(From Starting Out with Python, Chapter 3, Programming Exercises #8)

8. There are three seating categories at a stadium.  For a softball game,
Class A seats cost $15, Class B seats cost $12, and Class C seats cost $9.
Write a program that asks how many tickets for each class of seats were sold,
and then displays the amount of income generated from ticket sales.

For this exercise:

Example Output - Everything after the greater than sign (>) is user input:

Hi.  Let's see how much money the softball game made!
==========

How many Class A tickets ($15) were sold?
> 10
How many Class B tickets ($12) were sold?
> 10
How many Class C tickets ($9) were sold?
> 10
The total income is: $360!
"""

"""
Richie Doherty
2/4/20
CSCI-UA.0003-002 Section 1
"""
# Creating ticket prices
class_a = 15

class_b = 12

class_c = 9


# Asking user for input on how many Class A tickets were sold
sold_a = int(input("How many Class A tickets ($15) were sold? \n >")) #converting user input into string

#Generating the revenue from game for class a tickets
rev_a = sold_a * class_a

# Asking user for input on how many Class B tickets were sold
sold_b = int(input("How many Class B tickets ($12) were sold? \n >")) #converting user input into string

#Generating the revenue from game for class b tickets
rev_b = sold_b * class_b

# Asking user for input on how many Class C tickets were sold
sold_c = int(input("How many Class C tickets ($9) were sold? \n >")) #converting user input into string

#Generating the revenue from game for class c tickets
rev_c = sold_c * class_c

# Totaling all of the revenue from the game for all tickets
rev_t = rev_a + rev_b + rev_c

#printing total
print("The total income is: " + str(rev_t) + "!") #converting revenue total to a string

