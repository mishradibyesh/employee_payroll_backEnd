"""
@author: Dibyesh Mishra
@date: 02-01-2022 19:50
"""
from fastapi import FastAPI
from models import Employee
from connection import DbConnection
from queries import Functionality
import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG, format='%(asctime)s %(message)s')


function = Functionality()

app = FastAPI()

connection = DbConnection.establish_connection()
my_cursor = connection.cursor()


@app.get("/get_table")
async def get_table_data():
    """
    desc: created an api to retrieve all the data in the employee_table
    param: none
    return: employee details
    """
    try:
        message = function.show_table_data()
        logging.info("Successfully retrieved  Employee Details table")
        return {"status": 200, "message": "Successfully retrieved  Employee Details table", "data": message}
    except Exception as error:
        logging.error(f"error caught :{error}")
        print(error)


@app.post("/add_employee/")
def add_person(employee: Employee):
    """
    desc: created api to add one employee to the database
    param: employee class
    return: employee inserted details
    """
    try:
        function.add_employee_db(employee.employee_name, employee.profile_image, employee.employee_gender,
                                 employee.department, employee.salary, employee.start_date, employee.notes)
        logging.info("Successfully added Employee Details into table")
        return {"status": 200, "message": "Successfully added The Employee Details", "data": employee}
    except Exception as error:
        logging.error(f"error caught :{error}")
        print(error)


@app.put("/update_person_salary/")
def update_person(employee: Employee):
    """
    desc: created api to update one employee to the database
    param: employee class
    return: updated employee details
    """
    try:
        function.update_person_details(employee.salary, employee.employee_name)
        logging.info("updated  Employee Details table")
        return {"status": 200, "message": "Successfully updated the Employee Details", "data": employee.employee_name
                , "updated salary ": employee.salary}
    except Exception as error:
        logging.error(f"error caught :{error}")
        print(error)


@app.delete("/delete_person_by_name/")
def delete_person(employee: Employee):
    """
    desc: created api to delete one employee to the database
    param: employee class
    return: deleted employee details
    """
    try:
        function.delete_person_by_name(employee.employee_name)
        return {"status": 200, "message": "Successfully deleted one Employee Details", "data": employee.employee_name}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}
