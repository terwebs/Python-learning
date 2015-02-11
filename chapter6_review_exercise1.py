#Write a cube() function that takes a number and multiplies that number by itself twice
#over, returning the new value; test the function by displaying the result of calling your
#cube() function on a few different numbers

def cube(num):
    num = num ** 3
    return num

print cube(2)
print cube(3)

#Write a function multiply() that takes two numbers as inputs and multiples them
#together, returning the result; test your function by saving the result of multiply(2,
#5) in a new integer object and printing that integer’s value

def multi(num1, num2):
    multi_num = num1 * num2
    return multi_num

print multi(2,5)
