import sqlite3
import os
DIRPATH = os.path.dirname(__file__)
DBFILENAME = "question.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def _update(self):
        with sqlite3.connect(dbpath) as conn:
            curs = conn.cursor()
            SQL = """ UPDATE employees SET salary="$7300" WHERE lastname = "Reymin";"""
            curs.execute(SQL, employees)


def employee_for_state(state, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        SQL = """SELECT employees.lastname
        FROM employees JOIN branchs
        ON branchs.pk = employees.branch_pk
        WHERE branchs.state = ? AND SUBSTR(employees.salary,1)>=70000;"""


        cursor.execute(SQL, (state,))
        results = cursor.fetchall()

        return [result['lastname'] for result in results]
        
        

print(employee_for_state("NY"))
