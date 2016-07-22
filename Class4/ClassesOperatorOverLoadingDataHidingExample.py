__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/21/16'
__revision__ = '$'
__revision_date__ = '$'



class Marks:
    def __init__(self, marks, subject):
        print("inside constructor (__init__)")
        self.marks = marks
        self.subject = subject

    def __str__(self):
        print("inside constructor (__str__)")
        return 'Total marks %d obtained in %s ' % (self.marks, self.subject)

    def __add__(self,other):
        print("inside constructor (__add__)")
        return Marks(self.marks + other.marks, self.subject + ',' + other.subject)

m1 = Marks(80,"Subject 1")
m2 = Marks(85,"Subject 2")
m3 = Marks(75,"Subject 3")
m4 = Marks(83,"Subject 4")
m5 = Marks(82,"Subject 5")

print(m1 + m2 + m3 + m4 + m5)


class Parks:
    def __init__(self, marks, subject):
        print("Inside constructor (_init_)")
        self.marks = marks
        self.subject = subject

    def _str_(self):
        print("inside constructor (_str_)")
        return 'Total marks %d obtained in %s ' % (self.marks, self.subject)

    def __add__(self, other):
        print("Inside constructor (_add_)")
        return Marks(self.marks + other.marks, self.subject + ',' + other.subject)

m1 = Parks(80, "Math")
m2 = Parks(85, "Science")
m3 = Parks(75, "English")
m4 = Parks(83, "French")
m5 = Parks(82, "geography")

print( m1 + m2 + m3 + m4 + m5)



class Person(object):
    __secretCount = 0
    def getDetails(self):
        print("Calling Person Details method")
        self.__secretCount += 1
        print(self._Person__secretCount)

person1 = Person()
person1.getDetails()
person1.getDetails()
person1.getDetails()
person1.getDetails()
person1.getDetails()
