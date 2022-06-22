#! python3
#combinePdfs.py - Combines all the PDFs in the current working directory
# into a single PDF


import PyPDF2, os

os.chdir(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\minutes\combinedPdfs")

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\minutes\combinedPdfs"):
   if filename.endswith('.pdf'):
      pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()


# Loop through all the PDF files.
for filenames in pdfFiles:
   pdfFileObj = open(filename, 'rb')
   pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


   # Loop through all the pages (except the first) and add them.
   for pageNum in range(1, pdfReader.numPages):
      pageObj = pdfReader.getPage(pageNum)
      pdfWriter.addPage(pageObj)


# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
