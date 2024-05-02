#!/usr/bin/python3
""" Filtering the states by name """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            host="localhost",
            port=3306)
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states "
            "ORDER BY states.id ASC"
            )
    rows = cur.fetchall()
    for i in rows:
        if i[1][0] == 'N':
            print(i)
    cur.close()
    db.close()
