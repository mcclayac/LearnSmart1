__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/23/16'
__revision__ = '$'
__revision_date__ = '$'



from Class11RuntimeServices.sysconfigExample import sysConfig1, sysconfig2

# sysConfig1()
# sysconfig2()
#from Class11RuntimeServices.contextLibExamples import contextLib1

# contextLib1()


from  Class11RuntimeServices.contextLibExamples import function, myContext


print("Calling Function: ", function())

with myContext():
    print('The bit in the middle using my context')





