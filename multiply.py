"""
multiply.py
=====
Write a program that:

* asks the user for a number
* prints out a table of that number multiplied by the first 7 prime numbers:  
  2, 3, 5, 7, 11, 13, 17
* it will format the output so that the original number and the prime number are
  left aligned
* the product is right aligned
  * when using format, don't change the width to align the product
  * keep the width constant
* __COMMENT YOUR SOURCE CODE__ by 
   * briefly describing parts of your program 
   * include your name, the date, and your class section at top of your file 
     (above everything else)

Example interaction (everything after > is user input):
-----
Give me a number
> 17
17 * 2             34
17 * 3             51
17 * 5             85
17 * 7            119
17 * 11           187
17 * 13           221
17 * 17           289
"""

"""
Richie Doherty
2/4/20
CSCI-UA.0003-002 Section 1
"""
#Creating a list of the prime numbers
prime = [2,3,5,7,11,13,17]

#Asking user for input
number = int(input("give me a number")) #converting number to an integer since it will be returned as a string

#Naming the expression that will create the output based on our user's entry
result1 = number * prime[0] #I sliced into the prime list to call the 1st prime number

#Printing the first output of our table
print(format(str(number) + " * " + str(prime[0]), '<10') + format(str(result1), '>10'))
#Things to notice:
    #number, sliced prime and result are converted to strings
    # 2 format functions
        # 1st left aligns the inputted number and the prime number to the left with 10 characters
        # 2nd rigth aligns the outputed result to the right with 10 characters

#printing the 2nd output for our table
result2 = number * prime[1]  #I sliced into the prime list to call the 2nd prime number
print(format(str(number) + " * " + str(prime[1]), '<10') + format(str(result2), '>10'))

result3 = number * prime[2]   #I sliced into the prime list to call the 3rd prime number
print(format(str(number) + " * " + str(prime[2]), '<10') + format(str(result3), '>10'))

result4 = number * prime[3]
print(format(str(number) + " * " + str(prime[3]), '<10') + format(str(result4), '>10'))

result5 = number * prime[4]
print(format(str(number) + " * " + str(prime[4]), '<10') + format(str(result5), '>10'))

result6 = number * prime[5]
print(format(str(number) + " * " + str(prime[5]), '<10') + format(str(result6), '>10'))

result7 = number * prime[6]
print(format(str(number) + " * " + str(prime[6]), '<10') + format(str(result7), '>10'))
