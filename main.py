"""
@author: Dibyesh Mishra
@date: 02-01-2022 19:50
"""
from fastapi import FastAPI, Header
from models import Employee
from queries import Functionality
from token_for_id import TokenForLogin
import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
function = Functionality()
token_for_id = TokenForLogin()
app = FastAPI()


@app.get("/get_table/{table_name}")
async def get_table_data(table_name: str):
    """
    desc: created an api to retrieve all the data in the employee_table
    return: employee details
    """
    try:
        result = function.show_table_data(table_name)
        logging.info("Successfully retrieved  Employee Details table")
        return {"status": 200, "message": "Successfully retrieved  Employee Details table", "data": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.get("/get_data_by_id/{employee_id}")
async def get_employee_data(employee_id: int):
    """
    desc: created an api to retrieve all the data of the employee
    param: employee_id which is unique for each employee
    return: employee details in SMD format
    """
    try:
        result = function.show_employee_data(employee_id)
        logging.info("Successfully retrieved  Employee Details table")
        return {"status": 200, "message": "Successfully retrieved  Employee Details table", "data": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.post("/add_employee/")
async def add_employee(employee: Employee):
    """
    desc: created api to add one employee to the database
    param: employee class which have all the attributes related to employee
    return: employee inserted details
    """
    try:
        function.add_employee_db(employee.employee_id, employee.employee_name, employee.profile_image, employee.employee_gender,
                                 employee.department, employee.salary, employee.start_date, employee.notes)

        logging.info("Successfully added Employee Details into table")
        token_employee_id = token_for_id.encode_id(employee.employee_id)
        return {"status": 200, "message": "Successfully added The Employee Details",
                "token generated ": token_employee_id, "data": employee}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_salary/{employee_id}/{salary}")
async def update_employee_salary(employee_id: int, salary: int):
    """
    desc: created api to update one employee to the database
    param: employee_id ,employee_salary
    return: updated employee details in SMD format
    """
    try:
        result = function.update_person_salary(salary, employee_id)
        logging.info("updated salary of Employee Details table")
        return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_name/{employee_id}/{name}")
async def update_employee_name(employee_id: int, name: str):
    """
    desc: created api to update one employee name in the database
    param: employee_id , employee name
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_name(name, employee_id)
        logging.info(f"updated name of Employee_id {employee_id} in the table")
        return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_profile_img/{employee_id}/{profile_image}")
async def update_employee_profile_image(employee_id: int, profile_image):
    """
    desc: created api to update profile image of employee to the database
    param: employee id and profile image
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_profile_image(profile_image, employee_id)
        logging.info(f"updated profile photo of Employee_id {employee_id} ")
        return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_department/{employee_id}/{department}")
async def update_employee_department(employee_id: int, department: str):
    """
    desc: created api to update profile image of employee to the database
    param: employee id and department
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_department(department, employee_id)
        logging.info(f"updated department of Employee_id {employee_id} ")
        return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_gender/")
async def update_employee_gender(employee_id: int, gender: str):
    """
    desc: created api to update gender of employee to the database
    param: employee id and department
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_gender(gender, employee_id)
        logging.info(f"updated gender of Employee_id {employee_id} ")
        return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.delete("/delete_person_by_name/{employee_id}")
async def delete_employee_by_id(employee_id: int):
    """
    desc: created api to delete one employee to the database
    param: employee class which have all the attributes related to employee
    return: deleted employee details
    """
    try:
        function.delete_person_by_id(employee_id)
        logging.info(f"deleted employee by using Employee_id {employee_id}")
        return {"status": 200, "message": "Successfully deleted one Employee Details",
                "data": f"deleted employee id = {employee_id}"}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.post("/employee_login")
async def login_employee(token: str = Header(None)):
    employee_id = token_for_id.decode_id(token)
    employee_details = function.show_employee_data(employee_id)
    return employee_details