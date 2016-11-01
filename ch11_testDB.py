#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'mcclayac',
    'password': '11javajava',
    'host': '127.0.0.1',
    'database': 'employees'
}


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
    cur.execute('show databases;')
    for row in cur.fetchall():
        print(row)
finally:
    if cur:
        cur.close()
    if cnx:
        cnx.close()

#
# db = pymysql.connect("localhost","mcclay","11javajava","pythondb")
#
#
# cursor = db.cursor()
#
# cursor.execute("SELECT VERSION()")
#
#
# data = cursor.fetchone()
# print("Database version : %s " % data)
#
# db.close()
#


