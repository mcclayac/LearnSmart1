__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/23/16'
__revision__ = '$'
__revision_date__ = '$'


import atexit
from Class11RuntimeServices.exitHandlers import incrcounter, savecounter




print('registering')
atexit.register(incrcounter, 1)
atexit.register(savecounter)
print('registered ....')

