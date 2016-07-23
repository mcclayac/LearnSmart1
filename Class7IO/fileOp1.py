__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/23/16'
__revision__ = '$'
__revision_date__ = '$'


def fileOperations1():
    print("\nExmple program 1 - File Open\n")
    #Open a file
    file = open("example1.txt", "w")
    print("name of the file: ", file.name)
    print("Closed or not: ", file.closed)
    print("Opening Mode: ", file.mode)
    file.close()



def fileOperations2():
    print("\nExmple program 2 - File Write and close\n")
    #Open a file
    file = open("example1.txt", "w")
    file.write("Welcome to Python. \nHello World!!\n")
    file.close()

def fileOperations3():
    print("\nExmple program 3 - read file\n")
    file = open("example1.txt", "r")
    for line in file:
        print(line, end='')
    file.close()

def fileOperations4():
    print("\nExmple program 3 - rename file\n")
    import os
    os.rename("example1.txt", "example2.txt")
    file = open("example2.txt", "r")
    file.close()

def fileOperations5():
    print("This should create an error")
    file = open("example1.txt", 'r')
    print("Name of the file: ", file.name)

