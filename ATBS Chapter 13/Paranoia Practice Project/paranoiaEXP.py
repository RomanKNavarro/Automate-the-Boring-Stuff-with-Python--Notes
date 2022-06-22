#! python3

# paranoia.py - Encrypts every .pdf file in a given directory with a password provided through
# the command line, deletes the original file, and adds '_encrypted.pdf' to the file's original filename.

import os, shutil, PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

#directory = os.chdir(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\Paranoia Practice Project")
password = 'streetgang'

for folderName, subfolders, filenames in os.walk(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\Paranoia Practice Project\files 2"):
   os.chdir(folderName)
   for filename in filenames:
      if filename.endswith('.pdf'):

         #print(os.path.abspath(r'' + filename))
         #print(filename, '-ENCRYPTED\n')
         #print(os.path.basename(filename))
         pdfFile = open(os.path.basename(filename), 'rb')
         pdfReader = PyPDF2.PdfFileReader(pdfFile)
         '''pdfWriter = PyPDF2.PdfFileWriter()
         pdfWriter.appendPagesFromReader(pdfReader)

            
         filename2 = filename.replace('.pdf', '_encrypted.pdf')
         print(filename2)
         outputPdf = open(filename, 'wb')
         pdfWriter.write(outputPdf)
         pdfWriter.encrypt(password)
            

         shutil.move(os.path.abspath(outputPdf), os.path.abspath(filename2))


         pdfReader.close()
         pdfWriter.close()
         outputPdf.close()'''
            
                                
            

            

           
            
            
   
#C:\\Coding Shit\\myPrograms\\ATBS Chapter 13\\Paranoia Practice Project\\files 2\\minutescombinedminutes.pdf
#C:\Coding Shit\myPrograms\ATBS Chapter 13\Paranoia Practice Project\files 2\minutes\combinedminutes.pdf
