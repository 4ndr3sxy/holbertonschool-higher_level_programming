#!/usr/bin/python3
"""File to connect a DB using MySQLdb"""

import sys
import MySQLdb

if __name__ == "__main__":
    cities_string = ""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""
        SELECT cities.name
        FROM cities INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    info = cur.fetchall()

    for city in info:
        string_temporal = str(city)[2:-3]
        cities_string += string_temporal + ", "
    print(cities_string[:-2])

    cur.close()
    db.close()
