__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/23/16'
__revision__ = '$'
__revision_date__ = '$'


import atexit

try:
    print("Primer")
    _count = int(open("counter").read())
    print("Read _counter : ", _count)
    # print("Primer")
except IOError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    incrcounter(1)
    open("counter", "w").write("%d" % _count)
    print('count :', _count)

#
# print('registering')
# atexit.register(incrcounter, 1)
# atexit.register(savecounter)
# print('registered ....')
#
# 1