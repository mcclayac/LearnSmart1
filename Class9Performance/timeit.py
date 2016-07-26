__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/24/16'
__revision__ = '$'
__revision_date__ = '$'

import time

start_cpu = time.clock()
start_real = time.time()

from timeit import timeit

timeit('math.sqrt(2.0)', 'import math')
timeit('sqrt(2.0)', 'from math import sqrt')


end_cpu = time.clock()
end_real = time.time()


tmp2 = end_cpu - start_cpu
tmp1 = end_real - start_real

print("%f Real seconds" % (tmp1))
print("%f CPU seconds" % (tmp2))

