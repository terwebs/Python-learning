#Use a break statement to write a script that prompts the users for input repeatedly,
#only ending when the user types “q” or “Q” to quit the program; a common way of
#creating an infinite loop is to write while True:.


while True:
    word = raw_input('Enter "q" or "Q" to exit')
    if word == "q" or word == "Q":
        break

#Combine a for loop over a range() of numbers with the continue keyword to print
#every number from 1 through 50 except for multiples of 3; you will need to use the %
#operator.

for n in range(1, 51):
    # if n is divisor of 4 continue jumps to the next item of the loop
    if n % 3 == 0:
        continue
    else:
        print n
        
