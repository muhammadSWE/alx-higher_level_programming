#!/usr/bin/python3
"""script that takes argument and displays
values in the states"""
import MySQLdb
import sys

if __name__ == '__main__':    

    db = MySQLdb.connect(host='localhost', 
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
