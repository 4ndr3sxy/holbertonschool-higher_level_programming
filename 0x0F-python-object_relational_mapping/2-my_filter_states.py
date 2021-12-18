#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' \
    ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)

    info = cur.fetchall()

    for state in info:
        print(state)

    cur.close()
    db.close()
