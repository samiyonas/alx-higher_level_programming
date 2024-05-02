#!/usr/bin/python3
""" cities by states """
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
            "SELECT cities.id, cities.name, states.name FROM cities "
            "INNER JOIN states WHERE states.id = cities.state_id"
            )
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
