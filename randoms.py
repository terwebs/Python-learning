# print how many heads or tails resulted of flipping coins
from __future__ import division
from random import randint

heads = 0
tails = 0

flips = int(raw_input("How many times you have to flip de coin? :"))
for n in range ( 0, flips):
    if randint(0,1) == 0:
        tails += 1
    else:
        heads += 1

print "Heads: {}".format(heads)
print "Tails: {}".format(tails)

# Write a script that uses the randint() function to simulate the toss of a die, returning
# a random number between 1 and 6.

print "The dice toss result in :", randint (1,6)

#Write a script that simulates 10,000 throws of dice and displays the average number
#resulting from these tosses.

dice_result = 0
for n in range (0, 10000):
    dice_result = dice_result + randint(1,6)
print "the average is", dice_result / 10000

