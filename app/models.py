# database layer
#  we will create a model for our todo list, which will be a table in our database.
from . import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    age = db.Column(db.Integer, nullable=False)
    dept= db.Column(db.String(50),nullable=False)

    
    def __repr__(self):
        return f'<Employee {self.name}>'