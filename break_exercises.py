tries = 0

while tries < 3:
    password = raw_input("Password: ")
    if password == "Ih8biever":
        print "Password is correct"
        break
    else:
        tries += 1
else:
    print "Your account has been locked"
