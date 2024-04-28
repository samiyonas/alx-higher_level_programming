#!/usr/bin/python3
""" List all states from database using ORM """
from sys import argv
import MySQLdb
a1 = argv[1]
a2 = argv[2]
a3 = argv[3]
db = MySQLdb.connect(user=a1, passwd=a2, host="localhost", port=3306, db=a3)
cur = db.cursor()
if __name__ == "__main__":
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
