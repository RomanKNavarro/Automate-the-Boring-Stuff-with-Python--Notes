import os
totalSize = 0
for file in os.listdir(r'C:\Coding Shit\myPrograms'):
    totalSize += os.path.getsize(os.path.join(r'C:\Coding Shit\myPrograms', file))

'''Each file found in the path with "os.listdir()" is incremented to the end of the path
with "os.path.join()", and it's size, with the help of "getsize()", is added up to "totalSize".'''

print(str(totalSize) + ' megabytes')
                        
