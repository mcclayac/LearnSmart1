__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/16/16'
__revision__ = '$'
__revision_date__ = '$'


aList = [ 'physics','chemisry', 2010, 2014]
marksList = [80,82,73,64,85]

#  To print complete Lists
print("alist :", aList)
print("MarksList :", marksList)

# Print first Element in a list
print("alist[0] :", aList[0])
print("MarksList[0] :", marksList[0])

#Print MArks list 2nd to 3rd elements
print("MarksList[1:2] ", marksList[1:3])


aList[2] = 2011

#value at index 2
print("aList[2] :", aList[2])

print("Alist :", aList)
del aList[2]
print("First list length after deletion :", len(aList))
print("List after Deletion", aList)


#the total length of the list
aList = ['physics', 'chemistry', 2010, 2014];
print("First list length : ", len(aList))
print("Second list length : ", len(marksList))

# return items from the list with max value
print("Max value element : ", max(marksList))

# return items from the list with min value
print("min value element : ", min(marksList))