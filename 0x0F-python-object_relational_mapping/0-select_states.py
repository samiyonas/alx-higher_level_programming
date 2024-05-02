#!/usr/bin/python3
""" List all states from database using ORM """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], charset="utf8", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
