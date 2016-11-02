
import pymysql


db = pymysql.connect("localhost","mcclayac","11javajava","testdb")


cursor = db.cursor()

sql = """
INSERT
INTO
    testdb.student
    (
        FIRST_NAME,
        LAST_NAME,
        AGE,
        SEX,
        FEES
    )
    VALUES
    (
        'Lisa',
        'Johnson',
        20,
        'M',
        2000
    );
"""

try:
    cursor.execute(sql)
    db.commit()
    print("Row inserted")
except:
    db.rollback()
    print("Not Inserted")


# close the connection
db.close()
