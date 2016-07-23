__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/22/16'
__revision__ = '$'
__revision_date__ = '$'


def format1():
    print("Example Program 1")
    print("Format Method")
    print('{} to {} programming'.format('Welcome', 'Python'))


def format2():
    print("Example Program 2")
    print("Using formt() - a number in the brackets\n")
    print('{0} and {1}'.format('Input','Output'))
    print('{1} and {0}'.format('Input', 'Output'))

def format3():
    print("Example program #3")
    print("Format with named arguments")
    print('This {movie} is {adjective}'.format(movie='Gladiator', adjective='fantastic'))

def format4():
    print("Example of program #4")
    print("Keyword and position arguemnts")
    print('the story of {0}, {1}, and {other}'.format('Micheal', 'J', other="Junior"))


