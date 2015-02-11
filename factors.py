
def factor(number):
    for n in range(1,number + 1):
        # Returns the remainder of any division. ex since 4 is divisible by 2
        # 4 % 2 returns 0
        if number % n == 0:
            print "{} is a divisor of {}".format(n, number)
    return number

number = raw_input("Enter a positive integer:")
number = int(number)
factor(number)
