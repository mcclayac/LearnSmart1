__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/22/16'
__revision__ = '$'
__revision_date__ = '$'


print("\nOutput formatting - str() and repr() \n")


def example1():
    print("\nExample 1 - convert values to a string")
    var_str = 'Hello, World'

    # Convert values to a string
    print('str(var_str): ', str(var_str))
    print('repr(var_str): ', repr(var_str))
    print('str(22/7): ', str(22/7))
    print("\n\n")

    # repr() is to generate representations which can be read by the interpreter.
    # It will force a SyntaxError if there is no equivalent syntax.
    # str() is to return representations of values which are fairly human-readable.

def example2():
    var_a = 20 * 3.14
    var_b = 150 * 150
    var_str = 'The value of var_a is ' + repr(var_a) + ', and the var_b is ' + repr(var_b) + '...'
    print(var_str)
    # The repr() of a string adds string quotes and backslashes


def example3():
    print('\nExample 3 - The string can be read by the interpreter\n')
    var_str = 'Hello, world.\n'
    var_c = repr(var_str)
    print('repr(var_str): ', var_c)

def example4():
    print('\nExample 4 - The argument to repr method\n')
    var_a = 20 * 3.14
    var_b = 150 * 150
    # The argument to repr() may be any Python object
    print('repr((var_a, var_b, (\'Python\', \'Programming\'))): ', repr((var_a, var_b, ('Python', 'Programming'))))






