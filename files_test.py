my_input_file = open("text.txt", "r")
print "Line 0 (first line):", my_input_file.readline()

my_input_file.seek(0)
print my_input_file.readline()
print my_input_file.readline()

my_input_file.seek(8)
print "Line 0 (starting at 9th character):", my_input_file.readline()

my_input_file.close()

