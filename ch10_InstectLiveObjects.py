__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/23/16'
__revision__ = '$'
__revision_date__ = '$'

# !/usr/bin/python

# import inspect module
from inspect import signature


def sample(a, *, b: int, **kwargs):
    pass


sig = signature(sample)

print("sig : ", str(sig))
print("parameters['b'] : ", str(sig.parameters['b']))
print("annotation : ", sig.parameters['b'].annotation)

# modify paramter
new_sig = sig.replace(return_annotation="new return sig")

print("new sig : ", str(new_sig))

for param in sig.parameters.values():
    if (param.kind == param.KEYWORD_ONLY and param.default is param.empty):
        print('Parameter:', param)


def sample(a, *, b=10):
    pass


sig = signature(sample)
bind = sig.bind(10, b=15)

print("bind(10, b=15) : ", bind.args, bind.kwargs)

from inspect import formatargspec, getfullargspec

print("get full arg spec : ", formatargspec(*getfullargspec(sample)))