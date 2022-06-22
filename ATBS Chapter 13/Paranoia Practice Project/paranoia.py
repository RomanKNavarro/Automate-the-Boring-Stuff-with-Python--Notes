#! python3

# paranoia.py - Encrypts every .pdf file in a given directory with a password provided through
# the command line, deletes the original file, and adds '_encrypted.pdf' to the file's original filename.

import sys, os, shutil, PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

if len(sys.argv) < 2:
   print('paranoia.py - insert directory and password to encrypt .pdf files')
   sys.exit()

else:
   directory = os.chdir(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\Paranoia Practice Project\files\minutes")
   password = sys.argv[1]

   for folderName, subfolders, filenames in os.walk(str(directory)):
      for subfolder in subfolders:
         for filename in filenames:
            print(filename, '-ENCRYPTED')
            pdfReader = PyPDF2.PdfFileReader(open(os.path.abspath(filename)))
            pdfWriter = PyPDF2.pdfFileWriter()
            pdfWriter.appendPagesFromReader(pdfReader)

            
            filename2 = filename.replace('.pdf', '_encrypted.pdf')
            outputPdf = open(filename, 'wb')
            pdfWriter.write(outputPdf)
            pdfWriter.encrypt(password)
            

            shutil.move(os.path.abspath(outputPdf), os.path.abspath(filename2))


            pdfReader.close()
            pdfWriter.close()
            outputPdf.close()
            
                                
            

            

           
            
            
   
