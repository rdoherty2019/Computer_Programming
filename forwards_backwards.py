#setting accumulator
num = 0
print("Using while loops")

#Iterations
while num <31:
    #If number is divisably by 4 and 3
    if num % 4 == 0 and num % 3 == 0:
        #accumalte
        num += 3
        #continue to next iterations
        continue
    #IF number is divisable by 3 print
    if num % 3 == 0 :
        print(num)
    #accumulate
    num += 3

#Setting condition
nu = 30

while nu > 1:
    # If number is divisably by 4 and 3
    if nu % 4 == 0 and nu % 3 == 0:
        #reduce
        nu -= 3
        #conitune to next itteration
        continue
    # IF number is divisable by 3 print
    if nu % 3 == 0:
        print(nu)

    #reduce
    nu -= 3

print("Using for loops")

#setting range, making sure 30 is included
for n in range(3,31,3):

    if n % 4 == 0 and n % 3 == 0:
        continue
    if n % 3 == 0:
        print(n)
#setting range
#making sure 3 is included
#counting backwards
for n in range(30,2,-3):
    if n % 4 == 0 and n % 3 == 0:
        continue
    if n % 3 == 0 :
        print(n)