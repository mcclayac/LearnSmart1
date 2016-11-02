__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/1/16'
__revision__ = '$'
__revision_date__ = '$'



import pymysql


db = pymysql.connect("localhost","mcclayac","11javajava","testdb")


cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")

ddl = """

CREATE TABLE student (
                FIRST_NAME VARCHAR(50) NOT NULL,
                LAST_NAME VARCHAR(50),
                AGE INT,
                SEX VARCHAR(1),
                FEES FLOAT,
                PRIMARY KEY (FIRST_NAME)
);
"""


cursor.execute(ddl)
sql = "commit;"
cursor.execute(sql)


print("Table is created")

db.close()
