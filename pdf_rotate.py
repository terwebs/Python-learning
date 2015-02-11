import os
from pyPdf import PdfFileReader, PdfFileWriter

my_path = "D:/Training/Python-Learning/realpython-webster/Course1/Practice files_12"

input_file_name = os.path.join(my_path, "ugly.pdf")
input_file = PdfFileReader(file(input_file_name, "rb"))
output_PDF = PdfFileWriter()

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    if page_num % 2 == 0:
        page.rotateClockwise(90)
    
    output_PDF.addPage(page)

output_file_name = os.path.join(my_path, "ugly_test.pdf")
output_file = file(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()

