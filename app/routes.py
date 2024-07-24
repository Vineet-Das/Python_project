# routes and views for the flask application


from flask import  request, jsonify,Blueprint
from .models import Employee 
from .utils import get_data
import os
from . import db


from .schemas import EmployeeSchema


main= Blueprint('main',__name__)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

@main.route('/')
def index():
    return jsonify({"message":"WELCOME TO THE EMPLOYEE MANAGEMNET SYSTEM!"})
# CRUD - Create, Read, Update, Delete


@main.route('/employees', methods=['POST'])
def create_employee():


        user_data = request.get_json()
        errors = employee_schema.validate(user_data)
        if errors:
            return jsonify(errors),400
        
        employee_obj = Employee(id=user_data['id'],name=user_data['name'], age=user_data['age'],dept=user_data['dept'])
        db.session.add(employee_obj)
        db.session.commit()
        return jsonify({'message':'employee added successfully!!'})
        
    

    


# for getting the employess details
@main.route('/employees', methods=['GET'])
def get_employees():
        employee_data= Employee.query.all()
        data=get_data(employee_data)
        return jsonify(data)
        


   
    
# for get information of specific employee by id
@main.route('/employees/<int:id>',methods=['GET'])
def get_emp(id):
    employee_data=Employee.query.get(id)
    if not employee_data:
        os.abort(404,description="emp with id {id} is not found ")
    return jsonify([{'id':employee_data.id,'name':employee_data.name,'age':employee_data.age,'dept':employee_data.dept}])


# updating details of the employee
@main.route('/employees/<int:id>',methods=['PUT'])
def update_emp(id):
    employee=Employee.query.get(id)
    if not employee :
        return jsonify( description="employee not found" ),404
    data=request.get_json()
    employee.name=data['name']
    employee.age=data['age']
    employee.dept=data['dept']
    db.session.commit()
    return jsonify({"message":"updated sucessfully"})


# deleting employee's detail
@main.route('/employees/<int:id>',methods=['DELETE'])
def delete_emp(id):
    employee_data=Employee.query.get(id)
    if not employee_data:
        os.abort(404,description="emp with id {id} is not found ")
    db.session.delete(employee_data)
    db.session.commit()
    return jsonify({"message":"deleted successfully"})