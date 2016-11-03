#!/usr/bin/python3

from stat import *

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


def pathlib():

    print("Path Lib Functions")

    # Importing pathlib Library
    from pathlib import Path

    #Listing Subdirectories
    pathVariable = Path(".")

    [item for item in pathVariable.iterdir() if item.is_dir()]
    print("display path of directories : \n", [item for item in pathVariable.iterdir() if item.is_dir()] , "\n")

    for item in pathVariable.iterdir():
        if item.is_dir():
            posixPath = item
            name = posixPath.name
            print("dir: ", item, " ", name)

    # listing Python source files in this directory tree
    list(pathVariable.glob('*.py'))
    print("\nDisplay path of the files : ", list(pathVariable.glob('*.py')))

    # navigating inside a directory tree
    # pathVariable = Path('c:/python34/demo')
    # fileVariable = pathVariable / 'Module12' / '..'
    # print("\nDisplay path of the current file :", fileVariable)


    # listing Python source files in this directory tree
    # list(pathVariable.glob('*.py'))
    # print("\nDisplay path of the files : ", list(pathVariable.glob('*.py')))

    # querying path properties
    #print("\nWhether the path points to an existing file or directory : ", fileVariable.exists())

    # opening a file
    # with fileVariable.open() as file:
    #     line = file.readline()
    #     print("File content : ", line)
    #
    # file.close()




def dirtree(top, callback):
    """Recursively decend the directory tree rooted at the top
        calling the callback function for each regular file
    """
    # Imports
    import os, sys, stat


    for f in os.listdir(top):
        pathName = os.path(top, f)
        mode = os.stat(pathName).st_mode

        if S_ISDIR(mode):
            # It's a directory, recurse into it
            dirtree(pathName, callback)
        elif S_ISREG(mode):
            callback(pathName)
        else:
            print("Skipping %s" % pathName)

def visitFile(file):
    print("visiting", file)




def tempFile():
    print("\nExample program:\n")

    # to import tempfile module
    import tempfile

    # create a temporary file and write some data to it
    fp = tempfile.TemporaryFile()
    fp.write(b'Hello world!')

    # read data from file
    fp.seek(0)
    fp.read()

    # close the file, it will be removed
    fp.close()

    # create a temporary file using a context manager
    with tempfile.TemporaryFile() as fp:
        fp.write(b'Hello world!')
        fp.seek(0)
        fp.read()

    # file is now closed and removed
    # create a temporary directory using the context manager
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory: ', tmpdirname)

    # get temporary directory
    print("get temporary directory: ", tempfile.gettempdir())


def lzmaCompression():


    print("\nExample program:\n")

    # creating a compressed file
    import lzma
    data = b"Wellcome to Python"
    with lzma.open("example.xz", "w") as file:
        file.write(data)
    file.close()

    # reading in a compressed file
    with lzma.open("example.xz") as file:
        filecontent = file.read()
        print("\nContent in the file : ", filecontent)
    file.close()

    # compressing data in memory
    data_in = b"Wellcome to Python"
    data_out = lzma.compress(data_in)
    print("\nbefore Compress : ", data_in)
    print("\nafter Compress : ", data_out)

    # incremental compression
    lzcompression = lzma.LZMACompressor()
    out1 = lzcompression.compress(b"Some data\n")
    out2 = lzcompression.compress(b"Another piece of data\n")
    out3 = lzcompression.compress(b"Even more data\n")
    out4 = lzcompression.flush()

    # concatenate all the partial results:
    result = b"".join([out1, out2, out3, out4])
    print("\nresults:", result)

    data = b"This data will be compressed\n"

    # writing compressed data to an already-open file
    with open("example.xz", "wb") as file:
        with lzma.open(file, "w") as lzfile:
            lzfile.write(data)




def gzipCOmpression():
    # !/usr/bin/python

    print("\nExample program:\n")

    # to create a compressed GZIP file
    import gzip
    data = b"Wellcome to Python Programming"
    with gzip.open('example.txt.gz', 'wb') as file:
        file.write(data)

    file.close()

    # to read a compressed file
    with gzip.open('example.txt.gz', 'rb') as file:
        filecontent = file.read()
        print("File content : ", filecontent)
    file.close()

    # to GZIP compress an existing file
    with open('example.txt', 'rb') as filein:
        with gzip.open('example.txt.gz', 'wb') as fileout:
            fileout.writelines(filein)

    filein.close()
    fileout.close()

    # to GZIP compress a binary string
    inputString = b"Lots of content here"
    outputString = gzip.compress(inputString)
    print(" Input: ", inputString)
    print(" Output: ", outputString)




