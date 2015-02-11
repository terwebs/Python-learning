from capitals import capitals_dict
import random

# while true for infinite loop
while True:
    state = random.choice(capitals_dict.keys())
    capital = capitals_dict[state].lower()
    answer = raw_input("What is the capital of {}: ".format(state)).lower()
    if answer == capital:
        print "Correct"
        break
    elif answer == "exit":
        print "Goodbye"
        break
