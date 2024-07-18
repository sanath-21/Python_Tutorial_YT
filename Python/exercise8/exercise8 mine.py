# Write a program to manipulate pdf files using pyPDF. 
# Your programs should be able to merge multiple pdf files into a single pdf. 
# You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, 
# cropping, and transforming the pages of PDF files. 
# It can also add custom data, viewing options, and passwords to PDF files. 
# pypdf can retrieve text and metadata from PDFs as well.

import os
from pypdf import PdfWriter, PdfReader

merger = PdfWriter()
pdf_directory = "exercise8"
files = os.listdir(pdf_directory)
files.sort()
for file in files:
    if file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, file)   
        merger.append(pdf_path)

output = open("merged-pdf.pdf","wb")
merger.write(output)
merger.close()