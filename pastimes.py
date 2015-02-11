import csv
import os

my_path = "D:/Training/Python-Learning/realpython-webster/Course1"

with open(os.path.join(my_path, "pastimes.csv"), "rb") as my_file,
open (os.path.join(my_path, "categorized_pastimes.csv"), "wb") as out_file:
    my_file_reader = csv.reader(my_file)
    my_file_writer = csv.writer(out_file)
    
    next(my_file_reader)
    for row in my_file_reader:
        # determine if fighting is part of the string on row[1]
        if row[1].lower().find('fighting') != -1:
            row.append('Combat')
        else:
            row.append('Other')
        print row

        my_file_writer.writerow(row)
    

    
