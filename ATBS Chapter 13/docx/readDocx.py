#! python3

import docx, os

os.chdir(r"C:\Coding Shit\myPrograms\ATBS Chapter 13\docx")
def getText(filename):
   doc = docx.Document(filename)
   fullText = []
   for para in doc.paragraphs:
      fullText.append(para.text)
   return '\n'.join(fullText)

