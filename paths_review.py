# Display the full paths of all of the files and folders in the images folder by using
# os.listdir()

import glob
import os

my_path = "D:/Training/Python-Learning/realpython-webster/Course1/Practice files/images"

files_and_folders = os.listdir(my_path)
for folder_name in files_and_folders:
    full_path = os.path.join(my_path, folder_name)
    print full_path
    size = os.path.getsize(full_path)
    print size

print " "    
print " Display the full paths of any PNG files in the images folder by using glob.glob() "
print " "

file_names_list = os.listdir(my_path)

for file_name in file_names_list:
    if file_name.lower().endswith(".png"):
        print "Converting {} to jpg".format(file_name)
        full_file_name = os.path.join(my_path, file_name)
        new_file_name = full_file_name[0:len(full_file_name)-4]+".jpg"
        os.rename(full_file_name, new_file_name)
        print "converted into", file_name
        
    
    
files_and_folders = os.listdir(my_path)
for folder_name in files_and_folders:
    full_path = os.path.join(my_path, folder_name)
    if os.path.isdir(full_path):
        print folder_name
        
  
for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        print os.path.join(current_folder, file_name)
        
