## Byte Academy Phase 1 Assessment

Turn in by 4:30

You can use any source of information that is not a human being. 70% is a passing score.

If you get stuck, write comments describing how you think it should work and move on. Don't get bogged down on one problem. Do what you can for partial credit and move to work you know how to do. Come back if there is time at the end.

Your take-home portion is due to be turned in at the same time as the rest of the assessment.

#### Question 1: Get github user bio

Write a python program that inputs a github username and prints out that user's bio.

https://developer.github.com/v3/users/

(you do not need an access token for the endpoint to get general information from a username)

#### Question 2: Grid sum API

Write a flask API with one endpoint: "/sum" that receives json data from a POST request.

The data will be of the form
```
{
    "data": [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
}
```

It should sum the list of lists the key "data" refers to. And return a response like:

```
{
    "sum": 45
}
```

#### Question 3: Database

* Using python's sqlite3 module write a schema.py file that creates two database tables modeling the following:

    * Branch: A branch has a city, a state, and a zip code

    * Employee: An employee has a first name, a last name, an employee ID, and a salary

    * A branch has many employees, an employee works at one branch

Using INSERT statements in a seed.py file create two branches with four 
employees each using the following data:

```
# Flushing, NY 11368 branch has:

last name, first name, employee ID, salary

Lockett, Walker, S0001, $45000
Coleman, Casey, S0002, $70000
Kilome, Franklyn, S0003, $67000
Santiago, Hecton, S0004, $100000

# 3 branch has:

last name, first name, employee ID, salary

Valdez, Framber, S0005, $39000
Peacock, Brad, S0006, $51000
Guduan, Reymin, S0007, $67000
Cole, Gerrit, S0008, $55000
```

Write a SQL UPDATE statement to change Reymin Guduan's salary to 73000

Write a SQL SELECT statement to select all employees in New York that make over 70000 a year.

For full credit, write the SELECT statement without using a fixed pk in the query (don't use the fact that you know what the New York branch's pk is)

Your queries may be submitted as either SQL statements or Python code

#### Question 4: ORM Wrapper

Create ORM model subclasses for Branch and for Employee from the problem above.

Create a method for instances of Employee `instance.branch()` that returns the Branch object of the branch the employee works at. (This return should be of type Branch or None)

Write a unit test that tests that Branch works.

#### Submission (Bonus question)

* Create a new private repository on github and push your work to it. Add your instructor as a collaborator.

* Do not include python cache files, any virtual environments, or databases in your git repository. Use a .gitignore.

Submit the link. Do not post to the group chat, send the link in a private message.

* Proper submission is worth a bonus 10%. You can submit a zip, but you will not receive the bonus.

#### Good luck, you can do it!

* Thanks for a great phase 1!

* RUN YOUR CODE ONE LAST TIME BEFORE YOU SUBMIT!