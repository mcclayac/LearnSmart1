__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/21/16'
__revision__ = '$'
__revision_date__ = '$'


def fibo(num):
    vara,varb = 0, 1
    while varb < num:
        print(varb, end=' ')
        vara, varb = varb, vara + varb
    print()

def fibolist(num):
    result = []
    vara, varb = 0, 1
    while varb < num:
        result.append(varb)
        vara, varb = varb, vara + varb
    return result

