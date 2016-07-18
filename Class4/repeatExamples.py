__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/18/16'
__revision__ = '$'
__revision_date__ = '$'



#!/usr/bin/python
#While statement
#Example program 1
print("Example program 1\n")
count = 0
while (count < 5):
    print("The count in the loop is :", count)
    count = count + 1
print("Cameot of the loop, value of count is :", count, "Good bye")

# Arthmetic progression using the range method with for loop
print("Example program 2 \n")
for count in range(5):
    print("Inside for loop, count is:", count)
print("Came out of FOR LOOP, alue of count is", count, "Good Bye")


# Example Program 3
# Combination of an else statement with a for statement that searches for
# prime numbers from 10 to 20

#  to iterate between 10 to 20
for num in range (10,20):

    for increment in range (2, num):

        # to determine the first factor
        if (num % increment == 0):

            factor = num / increment
            print('%d equals %d * %d' % (num, increment, factor))

            #to move to the next number, the #first for
            break
    else:
        print(num, 'is a prime number')


# Example program 4
print("\nExample Program 3 - FOR with a BREAK construct \n")

for char in 'Python Programming':
    if char == 'h':
        continue
    print ('current character is : ', char)


#Example program 5
print("\nExample program 5 - Enumerate construct\n")
subjects = ['English', 'Mathematics', 'Science', 'History']
# start which defaults to 0
print(list(enumerate(subjects)))

print(list(enumerate(subjects, start=1)))

