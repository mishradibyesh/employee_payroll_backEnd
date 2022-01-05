"""
@author: Dibyesh Mishra
@date: 02-01-2022 19:49
"""
import logging
from connection import DbConnection


class Functionality:
    """
    class Functionality have methods which helping to manipulate the database table employee_details
    in database employee_payroll
    """
    connection = DbConnection.establish_connection()
    my_cursor = connection.cursor()

    def show_table_data(self):
        """
        desc: displaying the employee_details table
        return: data_list
        """
        try:
            query = "select * from employee_details"
            self.my_cursor.execute(query)
            data_list = [i for i in self.my_cursor]
            return data_list
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def show_employee_data(self, employee_id):
        """
        desc: displaying the employee_detail
        param: employee_id
        return: data_list
        """
        try:
            query = "select * from employee_details where employee_id = %d" % employee_id
            self.my_cursor.execute(query)
            data_list = [i for i in self.my_cursor]
            if data_list:
                return data_list
            else:
                return False
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def add_employee_db(self,employee_name, profile_image, employee_gender, department, salary, start_date, notes):
        """
        desc: adding employee details in  the employee_details table
        param : employee_name, profile_image, employee_gender, department, salary, start_date, notes
        return: message string
        """
        try:
            query = "insert into employee_details (employee_name, profile_image, employee_gender, department, salary," \
                    " start_date, notes) values ('%s', '%s', '%s', '%s', %d, '%s', '%s')" % (
                      employee_name, profile_image, employee_gender, department, salary, start_date, notes)
            self.my_cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def update_person_salary(self, salary, employee_id):
        """
        desc: updating employee details in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        try:
            query = "update employee_details set salary = %d where employee_id = %d " % (salary, employee_id)
            self.my_cursor.execute(query)
            self.connection.commit()
            updated_data = self.show_employee_data(employee_id)
            return updated_data
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def update_employee_profile_image(self, profile_image, employee_id):
        """
        desc: updating employee profile image in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        try:
            query = "update employee_details set profile_image = '%s' where employee_id = %d" % (profile_image,
                                                                                                 employee_id)
            self.my_cursor.execute(query)
            self.connection.commit()
            updated_data = self.show_employee_data(employee_id)
            return updated_data
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def update_employee_name(self, employee_name, employee_id):
        """
        desc: updating employee name in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        try:
            query = "update employee_details set profile_image = '%s' where employee_id = %d" % (employee_name,
                                                                                                 employee_id)
            self.my_cursor.execute(query)
            self.connection.commit()
            updated_data = self.show_employee_data(employee_id)
            return updated_data
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def update_employee_department(self, employee_department, employee_id):
        """
        desc: updating employee name in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        try:
            query = "update employee_details set department = '%s' where employee_id = %d" % (employee_department,
                                                                                                 employee_id)
            self.my_cursor.execute(query)
            self.connection.commit()
            updated_data = self.show_employee_data(employee_id)
            return updated_data
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def update_employee_gender(self, employee_gender, employee_id):
        """
        desc: updating employee gender in  the employee_details table
        param: gender, employee_name
        return: updated data or error
        """
        try:
            query = "update employee_details set employee_gender = '%s' where employee_id = %d" % (employee_gender,
                                                                                                   employee_id)
            self.my_cursor.execute(query)
            self.connection.commit()
            updated_data = self.show_employee_data(employee_id)
            return updated_data
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}

    def delete_person_by_id(self, employee_id):
        """
        desc: deleting employee details in  the employee_details table
        param: employee_name
        return: employee_id
        """
        try:
            query = "delete from employee_details where employee_id = %d" % employee_id
            self.my_cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            logging.error(f"error caught :{error}")
            return {"status": 500, "message": f"Error : {error}"}
