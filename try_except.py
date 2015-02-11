from __future__ import division

def divide (num1, num2):
    try:
        print num1 / num2
    except ( TypeError, ZeroDivisionError):
        print "Encountered a problem"

num1 = int(raw_input("Enter an non-zero integer: "))
num2 = int(raw_input("Enter an non-zero integer: "))
divide(num1, num2)



# Write a script that repeatedly asks the user to input an integer, displaying a message
# to “try again” by catching the ValueError that is raised if the user did not enter an
# integer; once the user enters an integer, the program should display the number back
# to the user and end without crashing

while True:
    try:
        number = int(raw_input("Enter a integer:"))
        print "the number you entered is: {}".format(number)
        break
    except ValueError:
        print "Try again"
