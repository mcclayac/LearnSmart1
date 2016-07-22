__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/18/16'
__revision__ = '$'
__revision_date__ = '$'



#!/usr/bin/python

def func(str):
    print("in funct :",  str)
    return

print("Example of program 1\n")

func("Python programming")

#  Default arguements

def func (subject, marks=100):
    # To print a passed string into function
    print("Subject Name", subject)
    print("Marks: ", marks)
    return

print("Example program 2 - using keywork arguments:\n")
func("Science", 80)

func("English")

func(marks=60, subject="Chemistry")

func(subject="Mathematics")


def func(args, *vartuple):
    # to print a string into a function
    print("output is: ")
    print(args)
    for var in vartuple:
        print(var)
    return

#now you can call user defined function
func(100)
func(70,80,90, 100)
