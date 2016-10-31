__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/30/16'
__revision__ = '$'
__revision_date__ = '$'


import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'mcclayac',
    'password': '11javajava',
    'host': '127.0.0.1',
    'database': 'employees'
}


query = ("SELECT emp_no, first_name, last_name, hire_date FROM employees ")


cnx = cur = None
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = cnx.cursor()
    # cur.execute('show databases;')
    # for row in cur.fetchall():
    #     print(row)
    # cur.execute('select * from users;')
    # for row in cur.fetchall():
    #     print(row)

    cur.execute(query)
    for (emp_no, first_name, last_name, hire_date) in cur:
        print("{}, {}, {} was hired on {:%d %b %Y}".format(
            emp_no, last_name, first_name, hire_date))

finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()
