__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/15/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/python

# Strings in Python

str = 'Hello World!'
strnew = "Python Programming"

# If you see a output message complete string
print(str)

# You will get the first character of the string
print("first character of the string: ", str[0])

# When required the string starting from 2nd to 5th
print("the string starting from 2nd to 5th: ",strnew[1:5])

# To access substrings, use the square brackets
# for slicing along with the index or indices to obtain your substring

# You can "update" an existing string by assigning a variable to another string.
strupdate = str[:6] + 'Python'
print("Updated String :- ", strupdate)

#to assign substring to be searched
sub = "P"


# The substring is searched between 0 to 10
print(strnew.count(sub))
print(strnew.count(sub,0,10))

# to specify the string to be searched
sub = "Prog"

# to print the index if found and -1 otherwise.
print(strnew.find(sub))

# to search starting index 5 and print the index if found and -1 otherwise.
print(strnew.find(sub, 5))

# to search starting index 50 and print the index if found and -1 otherwise.
print(strnew.find(sub, 50))

# assign separator string and get output as concatenation of the strings in the sequence seq

str = "-"
seq = ("Easy", "to", "Use")
print(str.join(seq))

# to get the length of the string
print(len(strnew))

strnew = "00000000Python Programming00000000"

# to print a copy of the string in which all chars have been stripped from the beginning and the end of the string.
print(strnew.strip( '0' ))

strnew = "Python Programming"
# to list of all the words in the string, using strnew as the separator (splits on all whitespace if left unspecified),
# optionally limiting the number of splits to num.
print(strnew.split( ))

# to replace a copy of the string with all occurrences of substring old replaced by new
strnew.replace("Python", "Perl")
