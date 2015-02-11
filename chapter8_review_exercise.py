#Write a script that prompts the user to enter a word using the raw_input() function,
#stores that input in a string object, and then displays whether the length of that string
#is less than 5 characters, greater than 5 characters, or equal to 5 characters by using a
#set of if, elif and else statements.

word = raw_input("Please enter a word:")
if len(word) > 5 :
    print "{} is greater than 5 characters".format(word)
    
elif len(word) < 5 :
    print "{} is less than 5 characters".format(word)
    
else:
    print "{} is equal to 5 characters".format(word)
