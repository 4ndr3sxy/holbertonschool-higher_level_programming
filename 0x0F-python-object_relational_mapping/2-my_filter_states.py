#!/usr/bin/python3
"""File to connect a DB using MySQLdb"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{:s}' \
    ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)

    info = cur.fetchall()

    for state in info:
        print(state)

    cur.close()
    db.close()
