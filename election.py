from __future__ import division
from random import random

candidate1 = 0
candidate2 = 0
a_wins = 0
b_wins =0

# loop for each region
for i in range (1, 4):
    average1 = 0
    average2 = 0
    
    # loop for elections  
    for n in range (0, 10000):
        candidate1 = random() * 100
        candidate2 = random() * 100
        average1 = average1 + candidate1
        average2 = average2 + candidate2

    average1 = average1 / 10000
    average2 = 100 - average1
    
    if average1 > average2 and average1 != average2:
        a_wins += 1
    else:
        b_wins += 1
        
    print "A has {}% chance of winning region {}".format(average1, i)
    print "B has {}% chance of winning region {}".format(average2, i)

    if a_wins == 2 or b_wins == 2:
        if a_wins > b_wins:
            print "The winning candidate is A"
        else:
            print "The winning candidate is B"
        break
  
        
    
