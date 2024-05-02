#!/usr/bin/python3
""" all cities by states """
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
            "SELECT cities.name FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id", (sys.argv[4],)
            )
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i != len(rows) - 1:
            print(rows[i][0], end=", ")
        else:
            print(rows[i][0])
    cur.close()
    db.close()
