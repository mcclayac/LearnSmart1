__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/23/16'
__revision__ = '$'
__revision_date__ = '$'


from Class11RuntimeServices.AbstractClassesExample import CompleteStack


cs = CompleteStack()
cs.push('Tony')
cs.push('Tyanne')
cs.push('Tyrone')
cs.push('Nina')
print(cs.pop())
print(cs.pop())
print(cs.size)



