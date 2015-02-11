import csv
import os

my_path = "D:/Training/Python-Learning/realpython-webster/Course1/Practice files"

high_scores = {}
with open(os.path.join(my_path, "scores.csv"), "rb") as my_file:
    my_file_reader = csv.reader(my_file)
    for name, score in my_file_reader:
        # convert score to int to check if is higher
        score = int(score)
        if name in high_scores:
            if score > high_scores[name]:
                # update the value to a higher score if the name already exists
                high_scores[name] = score
        else:
            high_scores[name] = score
    
    for name in sorted(high_scores):
        print name, high_scores[name]
        
        
    
