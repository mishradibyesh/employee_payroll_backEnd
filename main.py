"""
@author: Dibyesh Mishra
@date: 02-01-2022 19:50
"""
from fastapi import FastAPI
from models import Employee
from queries import Functionality
from custom_exception import DataNotFound
import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
function = Functionality()
app = FastAPI()


@app.get("/get_table")
async def get_table_data():
    """
    desc: created an api to retrieve all the data in the employee_table
    return: employee details
    """
    try:
        result = function.show_table_data()
        logging.info("Successfully retrieved  Employee Details table")
        if result == "":
            raise DataNotFound("Data can not retrieved")
        else:
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
        if not result:
            raise DataNotFound("Data can not retrieved or employee id does not exist")
        else:
            return {"status": 200, "message": "Successfully retrieved  Employee Details table", "data": result}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.post("/add_employee/")
async def add_person(employee: Employee):
    """
    desc: created api to add one employee to the database
    param: employee class which have all the attributes related to employee
    return: employee inserted details
    """
    try:
        result = function.add_employee_db(employee.employee_name, employee.profile_image, employee.employee_gender,
                                          employee.department, employee.salary, employee.start_date, employee.notes)
        if result:
            logging.info("Successfully added Employee Details into table")
            return {"status": 200, "message": "Successfully added The Employee Details", "data": employee}
        else:
            return {"status": 500, "message": f"Error : {result}"}

    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_salary/{employee_id}/{salary}")
async def update_person_salary(employee_id: int, salary: int):
    """
    desc: created api to update one employee to the database
    param: employee_id ,employee_salary
    return: updated employee details in SMD format
    """
    try:
        result = function.update_person_salary(salary, employee_id)
        if not result:
            raise Exception("Data can not retrieved or employee id does not exist")
        elif isinstance(result, list):
            logging.info("updated salary of Employee Details table")
            return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
        else:
            logging.info(f"error : {result}")
            return result
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_salary/{employee_id}/{name}")
async def update_person_name(employee_id: int, name: str):
    """
    desc: created api to update one employee name in the database
    param: employee_id , employee name
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_name(name, employee_id)
        if not result:
            raise Exception("Data can not retrieved or employee id does not exist")
        elif isinstance(result, list):
            logging.info(f"updated name of Employee_id {employee_id} in the table")
            return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
        else:
            logging.info(f"error : {result}")
            return result
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_profile_img/{employee_id}/{profile_image}")
async def update_person_profile_image(employee_id: int, profile_image):
    """
    desc: created api to update profile image of employee to the database
    param: employee id and profile image
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_profile_image(profile_image, employee_id)
        if not result:
            raise Exception("Data can not retrieved or employee id does not exist")
        elif isinstance(result, list):
            logging.info(f"updated profile photo of Employee_id {employee_id} ")
            return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
        else:
            logging.info(f"error : {result}")
            return result
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_department/{employee_id}/{department}")
async def update_person_department(employee_id: int, department: str):
    """
    desc: created api to update profile image of employee to the database
    param: employee id and department
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_department(department, employee_id)
        if not result:
            raise Exception("Data can not retrieved or employee id does not exist")
        elif isinstance(result, list):
            logging.info(f"updated department of Employee_id {employee_id} ")
            return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
        else:
            logging.info(f"error : {result}")
            return result
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.put("/update_person_gender/")
async def update_person_gender(employee_id: int, gender: str):
    """
    desc: created api to update gender of employee to the database
    param: employee id and department
    return: updated employee details in SMD format
    """
    try:
        result = function.update_employee_gender(gender, employee_id)
        if not result:
            raise Exception("Data can not retrieved or employee id does not exist")
        elif isinstance(result, list):
            logging.info(f"updated gender of Employee_id {employee_id} ")
            return {"status": 200, "message": "Successfully updated the Employee Details", "data ": result}
        else:
            logging.info(f"error : {result}")
            return result
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}


@app.delete("/delete_person_by_name/{employee_id}")
async def delete_person_by_id(employee_id):
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
