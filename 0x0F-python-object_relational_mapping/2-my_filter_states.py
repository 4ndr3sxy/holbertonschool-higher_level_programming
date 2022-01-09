#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    name = sys.argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""".format(name))

    info = cur.fetchall()

    for state in info:
        if state[1] == name:
            print(state)

    cur.close()
    db.close()
