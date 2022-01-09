#!/usr/bin/python3
"""lists all states with a name starting with N"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    info = cur.fetchall()

    for state in info:
        if state[1][0] == 'N':
            print(state)

    cur.close()
    db.close()
