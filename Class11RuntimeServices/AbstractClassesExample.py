__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/26/16'
__revision__ = '$'
__revision_date__ = '$'


from abc import ABCMeta, abstractmethod, abstractproperty

class Stackaable(metaclass=ABCMeta):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractproperty
    def size(self):
        pass

class Stack(Stackaable):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class CompleteStack(Stack):
    @property
    def size(self):
        return len(self.items)



