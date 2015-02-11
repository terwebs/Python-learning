#In one line, display the result of trying to find() the substring “a” in the string “AAA”;
#the result should be -1

print "AAA".find("a")

#Create a string object that contains the value “version 2.0”; find() the first occurrence
#of the number 2.0 inside of this string by first creating a “float” object that stores the
#value 2.0 as a floating-point number, then converting that object to a string using the
#str() function

version = "version 2.0"
version_float = 2.0
print version.find(str(version_float))

#Write and test a script that accepts user input using raw_input(), then displays the
#result of trying to find() a particular letter in that input

test = raw_input("please enter a word: ")
print test.find(raw_input("enter a letter of the word you just used: "))
