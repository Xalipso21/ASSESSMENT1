import unittest
import schema, seed
from question4.orm import ORM
from question4.employee import Employee
from question4.branch import Branch


import os

Employee.dbpath = "question.db"


class TestEmployee(unittest.TestCase):

    def testBranchFor(self):
        test = Employee.branch_for("Valdez")
        self.assertEqual(test,"Houston, TX, 77002" , "Branch works")

   
