def invest(amount, rate, time):
    print "Principal amount: ${}".format(amount)
    print "annual rate of return: ${}".format(rate)
    for n in range (1, time + 1):
        amount = amount * rate + amount
        print "year {}: ${}".format(n, amount)
    return amount

amount = raw_input("Please enter the amount of the investment: ")
amount = float(amount)
rate = raw_input("Please enter the annual rate: ")
rate = float(rate)
time = raw_input("Please enter number of years: ")
time = int(time)

invest(amount, rate, time)
