__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/23/16'
__revision__ = '$'
__revision_date__ = '$'


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def example1():
    print("Example #1")
    try:
        raise MyError(10*10)
    except MyError as e:
        print("My own defined exception occurred, value: ", e.value)


def example2():
    print("Example #2")
    try:
        raise NameError('Hi, There')
    except NameError as e:
        print('An Exception flex by!', e)
        raise


