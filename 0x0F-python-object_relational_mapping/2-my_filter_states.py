#!/usr/bin/python3
""" filter states by user input """
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
    query = "WHERE states.name = '{}' ".format(sys.argv[4])
    cur.execute(
            "SELECT * FROM states " +
            query +
            "ORDER BY states.id ASC"
            )
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
