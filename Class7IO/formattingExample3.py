__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/22/16'
__revision__ = '$'
__revision_date__ = '$'


import math



# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be
# used to convert the value before it is formatted.


def formatMath1():
    print('The value of pi is approximatly {}.'.format(math.pi))
    print('The value of pi is approximatly {!r}.'.format(math.pi))
    print('The value of pi is approximatly {!a}.'.format(math.pi))
    print('The value of pi is approximatly {!s}.'.format(math.pi))

# An optional ':' and format specifier can follow the field name.
# This allows greater control over how the value is formatted.
# rounds Pi to three places after the decimal.

def formatMath2():
    print("\nExample program 2 - Using format() control over the value\n")
    print('The value of PI is approximately {0:.3f}.'.format(math.pi))

    table = {'Lauren': 2000, 'Nick': 4000, 'Andrew': 3000}
    for name, ECode in table.items():
        print('{0:10} ==> {1:10d}'.format(name, ECode))

def formatMath3():
    print("\nExample program 3 - Values formatted by name instead of position\n")
    table = {'Lauren': 2000, 'Nick': 4000, 'Andrew': 300000}
    print('Nick: {0[Nick]:d}; Lauren: {0[Lauren]:d}; '
          'Andrew: {0[Andrew]:d}'.format(table))

def formatMath4():
    # The % operator can also be used for string formatting. It interprets the left argument much like a
    # sprintf()-style format string to be applied to the right argument, and returns the string
    # resulting from this formatting operation.

    print("\nExample program 4 - String formatting using % operator\n")
    print('The value of PI is approximately %5.3f.' % math.pi)