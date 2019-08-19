import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "question.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def seed(dbpath):
    employees = [
            ("Lockett", "Walker", "S0001", "$45000",1),         # pk 1
            ("Coleman", "Casey", "S0002", "$70000",1),         # pk 2
            ("Kilome", "Franklyn", "S0003", "$67000",1),  # pk 3
            ("Santiago", "Hecton", "S0004", "$100000",1),         # pk 4
            ("Valdez", "Framber", "S0005", "$39000",2),
            ("Peacock", "Brad", "S0006", "$51000",2),
            ("Guduan", "Reymin", "S0007", "$67000",2),
            ("Cole", "Gerrit", "S0008", "$55000",2)]            

    branchs = [
            ("Flushing","NY", 11368), # pk 1,
            ("Houston", "TX", 77002)] # pk 2


    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        SQL = """INSERT INTO employees(firstname, lastname,employee_id,salary,branch_pk) VALUES(?,?,?,?,?);"""
        for employee in employees:
            cursor.execute(SQL, employee)
        
        SQL = """INSERT INTO branchs(city,state,zipcode) VALUES(?,?,?);"""
        for branch in branchs:
            cursor.execute(SQL, branch)
        
if __name__ == "__main__":
    seed(DBPATH)