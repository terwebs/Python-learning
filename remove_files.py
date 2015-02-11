import os

my_path = "D:/Training/Python-Learning/realpython-webster/Course1/Practice files/little pics"
# look in folders and subfolders
for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        full_path = os.path.join(current_folder, file_name)
        # check if the size is less than 200 and ends with .jpg
        if os.path.getsize(full_path) < 2000 and full_path.endswith(".jpg"):
            os.remove(full_path)
