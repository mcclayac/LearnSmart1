__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/21/16'
__revision__ = '$'
__revision_date__ = '$'


class Person(object):
    def __init__(self, name):
        print("Calling Person constructor")
        self.name = name

    def getDetails(self):
        print("Calling the Person Details method")
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        print("Calling Student constructor")
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def getDetails(self):
        print("Calling Student Details method")
        return "%s studies %s and in %s year" % (self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        print("Calling teacher constructor")
        Person.__init__(self, name)
        self.papers = papers


    def getDetails(self):
        print("Calling Teacher Details method")
        return "%s papers %s " % (self.name, self.papers)

person1 = Person("Tyler")
print(person1.getDetails())

student1 = Student('Ryan','Computer Science', 2013)
print(student1.getDetails())

teacher1 = Teacher('Matthew', ['C', 'C++'])
print(teacher1.getDetails())


