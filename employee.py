import sqlite3
from question4.orm import ORM
from question4.branch import Branch


class Employee(ORM):
    dbpath = ""
    tablename = "employees"

    fields = ['firstname','lastname','employee_id', 'branch_pk',]

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")
        self.employee_id = kwargs.get("employee_id")
        self.branch_pk = kwargs.get("branch_pk")

    
    @classmethod
    def branch_for(self, lastname):
        
        branch = Branch.one_from_where_clause("WHERE lastname=? AND branch_pk=?", (lastname, self.pk))
        if branch is None:
            return None
        return branch