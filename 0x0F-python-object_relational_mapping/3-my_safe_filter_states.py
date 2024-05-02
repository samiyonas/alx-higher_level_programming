#!/usr/bin/python3
""" SQL injection """
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
            "WHERE states.name = %s "
            "ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for i in rows:
        if i[1] == sys.argv[4]:
            print(i)
    cur.close()
    db.close()
