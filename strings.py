#!/usr/bin/python

# Lists in Python

list = [ 'Python Programming', 100 , 92.75, 'john', 82.3 ] 
tinylist = [80, 82, 73, 64, 85 ]

# to print complete list
print("list: ", list)
print("tinylist: ", tinylist)

# to print first element of the list
print("list[0]: ", list[0])
# to print elements starting from 2nd till 3rd
print("list[1:3]: ", list[1:3])

# to print elements starting from 3rd element
print("print elements starting from 3rd element : ")
print(list[2:])

# to print list two times
print("list two times: ", tinylist * 2)

# to print concatenated lists
print("concatenated lists: ", list + tinylist )