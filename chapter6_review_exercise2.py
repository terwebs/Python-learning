#Write a for loop that prints out the integers 2 through 10, each on a new line, by using
#the range() function

for n in range (2, 10):
    print n
print "end of the for loop"

#Use a while loop that prints out the integers 2 through 10 (Hint: you’ll need to create
#a new integer first; there’s no good reason to use a while loop instead of a for loop in
#this case, but it’s good practice…)

n = 2
while (n < 10):
    print n
    n = n + 1
print "end of the while loop"
    
#Write a function doubles() that takes one number as its input and doubles that number
#three times using a loop, displaying each result on a separate line; test your function
#by calling doubles(2) to display 4, 8, and 16

def doubles(number):
    for n in range (0, 3):
        number = number * 2
        print number
    return number

doubles(2) 
