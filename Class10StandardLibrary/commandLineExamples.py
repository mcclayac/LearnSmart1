__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/24/16'
__revision__ = '$'
__revision_date__ = '$'


def commandLine1():
    import sys
    print(sys.argv)

    print('\n-----------------------------------------\n')
    for arg in sys.argv:
        print(arg)

    print('\n ------sys.stderr.write ---------\n')
    sys.stderr.write('Warning, log file not found, starting a new one \n')



def commandLine2():
    import re
    print("find all:", re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
    print("sub String:", re.sub(r'(ba-z+) \1', r'\1', 'cat in the the hat'))
    print("replace:",  'tea for too'.replace('too', 'two'))


def commandline3():
    import math
    print('cos of pi/4', math.cos(math.pi / 4))
    print('Log of 1024', math.log(1024, 2))

def commandLine4():
    import random

    print("Random choice first: ", random.choice(['one', 'two', 'three', 'four', 'five', 'six', 'seven']))
    print("Random choice second: ", random.choice(['one', 'two', 'three', 'four', 'five', 'six', 'seven']))
    print("Random choice third: ", random.choice(['one', 'two', 'three', 'four', 'five', 'six', 'seven']))
    print('Sampling without replacement', random.sample(range(100), 10 ))
    print("Random float with Random()", random.random())
    print("Random Integer from range", random.randrange(4))
    print("Random choice fourth: ", random.choice(['one', 'two', 'three', 'four', 'five', 'six', 'seven']))





