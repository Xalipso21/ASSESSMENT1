import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'question.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = "DROP TABLE IF EXISTS branchs;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE branchs (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            state TEXT,
            zipcode INTEGER 
        ); """
        cur.execute(SQL)

        SQL = "DROP TABLE IF EXISTS employees;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE employees (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            salary VARCHAR(20),
            employee_id VARCHAR(20),
            branch_pk,
            FOREIGN KEY(branch_pk) REFERENCES branchs(pk)
        ); """
        cur.execute(SQL)

if __name__ == "__main__":
    schema(DBPATH)
