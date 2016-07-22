__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/21/16'
__revision__ = '$'
__revision_date__ = '$'




import class5.fibonacci

class5.fibonacci.fibo(50)


print("  ", class5.fibonacci.fibolist(80))


from class5.fibonacci import fibolist, fibo

fibo(400)
print(" ", fibolist(500))


from class5.fibonacci import *
fibo(200)

print(" ", fibolist(300))

fib = class5.fibonacci.fibo

print("dir(fib) :", dir(fib))

print("\n\n")

print("dir():", dir())

