__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/16/16'
__revision__ = '$'
__revision_date__ = '$'


aTup = ('physics','chemistry',2010, 2014)
bTup = (80,82,73,64,85)

#Print fuples
print("atup :", aTup)
print("btup :", bTup)

print("atup[0] :", aTup[0])
print("btup[0] :", bTup[0])



# to print elements starting from 2nd to 4th
print("bTup[1:3]: ", bTup[1:4])

print("Value available at index 2 : ")
print(aTup[2])

# Not valid action to the tuple
# aTup[2] = 2011

# Instead of assign create a new variable.
cTup = aTup[0:1] + bTup[1:3]

print("New Tuple : ")
print(cTup)

#the total length of the tuple

print("First tuple length : ", len(aTup))
print("Second tuple length : ", len(bTup))

# return items from the tuple with max value
print("Max value element : ", max(bTup))

# return items from the tuple with min value
print("min value element : ", min(bTup))

# Convert a tuple to a list
listtup = list(aTup)
print("List elements from Tuple: ", listtup)

# Removing individual tuple elements is not possible
# del aTup[2]

del aTup
print("After deleting tuple : ")
print(aTup)