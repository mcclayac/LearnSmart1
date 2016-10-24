__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/23/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/python

code = compile('a + 5', 'file.py', 'eval')
a = 5

print("code : ", eval(code))

# import parser module
import parser

st = parser.expr('b + 5')
code = st.compile('file.py')
b = 15

print("Parser code : ", eval(code))

# import systable module - access to the compilerâ€™s symbol tables
import symtable

table = symtable.symtable("def func(): pass", "string", "exec")

print("func :", table.lookup("func").is_namespace())
