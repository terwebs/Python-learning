from __future__ import division
from random import randint

trials = 1
flips = 0
heads = 0
tails = 1

for n in range(trials):
    first_flip = randint(0, 1)
    # Track our first flip
    flips = flips + 1

    # Keep flipping until we get a different result
    while True:
        flips += 1
        
        if randint(0,1) != first_flip:
            break

print "Number of flips: {}".format(flips)
# Print the average number of flips
print "the average number of flips was: {}".format(flips / trials)


