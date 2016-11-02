#!/usr/bin/python3



def fileObjectsWrite():

    print("Example Program")

    # Open a File
    file = open("example.txt", "w")
    print("Namr of file : ", file.name)



    fileid = file.fileno()
    print("File Desciptor ID : ", fileid)


    print("\nExample program 2 :\n")

    file.write("""Welcome to Python.\n Hello World!! \nThis is the third line.\nthis is the 4th line\nThis is the 5th line\n""")

    sequence = ["this is the 6th line\n", "this is the 7th line\n"]

    #write lines at the end of the file
    file.seek(0,2)
    line = file.writelines( sequence )

    file.close()



def fileObjectsRead():

    print("Examle Program Read")
    file = open("example.txt","r")

    # returns the next input line, or raises StopIteration when EOF is hit
    for index in range(3):
        row = file.__next__()
        print("Line no %d - %s" % (index, row))

    # number of bytes to read from the file
    readLine = file.readline(5)

    print("Read 5 bytes: %s" % readLine)
    file.close()


    file = open("example.txt","r")
    readLines = file.readlines()
    print("\nRead Lines: %s" % (readLines))

    readLines = file.readline(15)
    print("\nRead Lines Aproximatly 15 bytes : %s" % readLines)


def fileAccessibility():
    import os, sys, stat

    # Test the exisitance
    returnValue = os.access("example.txt", os.F_OK)
    print("F_OK - return value %s" % returnValue)

    # Test if ok to read
    returnValue = os.access("example.txt", os.R_OK)
    print("R_OK - return value %s" % returnValue)

    # Test if ok to write
    returnValue = os.access("example.txt", os.W_OK)
    print("W_OK - return value %s" % returnValue)


    # Test if ok to execute
    returnValue = os.access("example.txt", os.X_OK)
    print("X_OK - return value %s" % returnValue)

    #  Sets group executable
    os.chmod("example.txt", stat.S_IXGRP)


    #set other can write
    os.chmod('example.txt', stat.S_IWOTH )

    #

