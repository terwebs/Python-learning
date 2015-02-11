import os
from pyPdf import PdfFileReader

my_path = "D:/Training/Python-Learning/realpython-webster/Course1/Practice files_12"

input_file_name = os.path.join(my_path, "half and half.pdf")
input_file = PdfFileReader(file(input_file_name, "rb"))
page = input_file.getPage(0)
print page.mediaBox
