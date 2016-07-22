__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/21/16'
__revision__ = '$'
__revision_date__ = '$'


print("\nExample Program 1 : Classes and Instances")
class Student:
    'common base class for all students'
    studentCount = 0
    def __init__(self, name, fee, age):
        self.name = name
        self.fee = fee
        self.age = age
        Student.studentCount += 1

    def displayCount(self):
        print("Total Students %d" % Student.studentCount)

    def dispayStudent(self):
        print("Name:", self.name, " fee: ", self.fee, " age:", self.age)

    def displayAge(self):
        print("Name:", self.name, " age:", self.age)

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, ' destroyed')

student1 = Student("eddy", 2500, 17)
student1.dispayStudent()
student1.displayAge()


print("\nExample Program 2 : Classes and Instances")
print("hasattr: ", hasattr(student1, 'age'))
print("getattr: ", getattr(student1, 'age'))
print("setattr: ", setattr(student1, 'age', 33))
student1.dispayStudent()

#print("delattr: ", delattr(student1, 'age')) # Delete attribute 'age'
#print("hasattr: ", hasattr(student1, 'age')) # Returns true if 'age' attribute exists




'Built-in class attributes'
print("\n\nStudent.__doc__:", Student.__doc__)
print("\n\nStudent.__name__:", Student.__name__)
print("\n\nStudent.__module__:", Student.__module__)
print("\n\nStudent.__bases__:", Student.__bases__)
print("\n\nStudent.__dict__:", Student.__dict__)

print("Total Students %d" % Student.studentCount)

print('Destroying Objects (Garbage Collection)')
print("Object id: ", id(student1))

del student1

# You can add, remove or modify attributes of classes and objects at any time
# student1 = Student("Ebby", 2500, 17)
# student1.department = "Computer Science"  # Add a department attribute
# student1.department = "Chemistry"         # Modify department attribute
# del student1.department                   # Delete department attribute
