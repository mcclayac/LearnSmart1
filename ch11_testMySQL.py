

import pymysql


db = pymysql.connect("localhost","mcclayac","11javajava","testdb")


cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database Verson : %s" % data)

db.close()


