import os
from pyPdf import PdfFileReader, PdfFileWriter

my_path = "D:/Training/Python-Learning/realpython-webster/Course1/Practice files_12"

input_file_name = os.path.join(my_path, "Pride and Prejudice.pdf")
input_file = PdfFileReader(file(input_file_name, "rb"))
output_PDF = PdfFileWriter()

for page_num in range(1,4):
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name = os.path.join(my_path, "Output/portion.pdf")
output_file = file(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
