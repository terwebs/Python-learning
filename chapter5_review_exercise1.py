#Create a string object that stores an integer as its value, then convert that string into
#an actual integer object using int(); test that your new object is really a number by
#multiplying it by another number and displaying the result

number = "2"
number = int(number)
print number * 2

#Repeat the previous exercise, but use a floating-point number and float()

number_float = "2"
number_float = float(number)
print number_float * 2

#Create a string object and an integer object, then display them side-by-side with a single
#print statement by using the str() function

string = "2"
print string + str(number)
