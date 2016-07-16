__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/16/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/python

# Open a file
file = open("example.txt", "w")
print("Name of the file: ", file.name)
print("Closed or not : ", file.closed)
print("Opening mode : ", file.mode)

file.write("Welcome to Python.\nHello World!!\n")

# Close opened file
file.close()
import os
# Rename a file from example.txt to example1.txt
os.rename( "example.txt", "example1.txt" )
file = open("example1.txt", "r")
print("Name of the file: ", file.name)


file = open("example1.txt", "r")
# read the file
for line in file:
    print(line, end='')


# After renamed the file example.txt will be not available.
# So, error will occur.
#file = open("example.txt", "r")
#print("Name of the file: ", file.name)
