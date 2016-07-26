__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/23/16'
__revision__ = '$'
__revision_date__ = '$'


def withExample1():
    print("Example program #1\n")
    for line in open("/mcclayac/pythoncode/LearnSmart1/Class8Exceptions/myfile1.txt"):
        print(line, end="")



def withExample2():
    print("\n\nExample program #2\n")
    with open("/mcclayac/pythoncode/LearnSmart1/Class8Exceptions/myfile1.txt") as f:
        for line in f:
            print(line, end="")


