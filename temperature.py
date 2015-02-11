from __future__ import division

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

celsius = raw_input("please enter the temperature in celsius:")
celsius = int(celsius)
print "{} degress C = {} degress F".format(celsius, celsius_to_fahrenheit(celsius) )

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32)*5/9
    return celcius

fahrenheit = raw_input("please enter the temperature in fahrenheit:")
fahrenheit = int(fahrenheit)
print "{} degress F = {} degress C".format(fahrenheit, fahrenheit_to_celcius(fahrenheit) )
    
