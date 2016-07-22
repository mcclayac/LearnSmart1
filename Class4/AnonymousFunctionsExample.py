__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/18/16'
__revision__ = '$'
__revision_date__ = '$'


# Anonmymous FUnctions lambda

print("Example program 1 - Anonmous function Lambda:\n")
total = lambda sub1, sub2, sub3,sub4, sub5: sub1 + sub2 + sub3 + sub4 + sub5

# Now you can call the function
print("Student1 Marks of the tptal :", total(70,80,90,80,85))
print("Student2 Marks of the tptal :", total(90,85,95,85,95))
print("Student3 Marks of the tptal :", total(30,40,55,66,77))

def func_ref( list ):
    print("List value omside the function before append", list)
    list.append([90, 75, 68, 84])
    print("values inside function after append", list)
    return

list = [60,70,80]
print("Example 2 program : Pass by assignment\n")
print("List the values before calling the function:", list)

func_ref(list)
print("List the values after the functiomn", list)

