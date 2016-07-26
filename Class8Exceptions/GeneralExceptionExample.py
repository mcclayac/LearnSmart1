__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/23/16'
__revision__ = '$'
__revision_date__ = '$'


def divisionByZero():
    x = 90 * (1/0)



def stringExample():
    x = '75' + 25

def nameexample():
    x = 75 + vara * 30   # (nameError: vara is not defined

def trycatchExample1():
    while True:
        try:
            x = int(input('Please enter a number: '))
            break
        except ValueError:
            print("No! that was not a valid number. try again .....")


def trycatchExample2():
    import sys

    try:
        #open file myfile
        file = open('/mcclayac/pythoncode/LearnSmart1/Class8Exceptions/myfile1.txt', 'r')
        str = file.readline()
        vara = int(str.strip())
        print( vara * 2)

    except OSError as err:
        print("OS Error {}".format(err))
    except ValueError:
        print("Could not convert dta into an integer")
    except :
        print("Unexpected Error: ", sys.exc_info()[0])
        raise


