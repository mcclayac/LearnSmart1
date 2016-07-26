__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/23/16'
__revision__ = '$'
__revision_date__ = '$'


def exampleTry1(x, y):
    print("\n\nExample 1 - try else finally example")
    try:
        result =  x / y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("Result is, ", result)
    finally:
        print("executing finally clause")


def exampleTry2():
    print("\n\nExample 2 - cleanup actions")

    try:
        raise KeyboardInterrupt
    finally:
        print('Good Bye!')
