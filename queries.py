"""
@author: Dibyesh Mishra
@date: 02-01-2022 19:49
"""
from connection import DbConnection
from custom_exception import DataNotFound


class Functionality:
    """
    class Functionality have methods which helping to manipulate the database table employee_details
    in database employee_payroll
    """
    connection = DbConnection.establish_connection()
    my_cursor = connection.cursor()

    def show_table_data(self, table_name):
        """
        desc: displaying the employee_details table
        return: data_list
        """

        query = "select * from %s " % table_name
        self.my_cursor.execute(query)
        data_list = [i for i in self.my_cursor]
        if data_list:
            return data_list
        else:
            raise DataNotFound("table  is not present in the database")

    def show_employee_data(self, employee_id):
        """
        desc: displaying the employee_detail
        param: employee_id
        return: data_list or error
        """
        query = "select * from employee_details where employee_id = %d" % employee_id
        self.my_cursor.execute(query)
        data_list = [i for i in self.my_cursor]
        if data_list:
            return data_list
        else:
            raise DataNotFound("this id is not present in the database")

    def add_employee_db(self, employee_id: int, employee_name, profile_image, employee_gender, department, salary,
                        start_date, notes):
        """
        desc: adding employee details in  the employee_details table
        param : employee_name, profile_image, employee_gender, department, salary, start_date, notes
        return: message string
        """
        query = "insert into employee_details (employee_id, employee_name, profile_image, employee_gender, department," \
                " salary, start_date, notes) values (%d, '%s', '%s', '%s', '%s', %d, '%s', '%s')" % (employee_id,
                      employee_name, profile_image, employee_gender, department, salary, start_date, notes)
        self.my_cursor.execute(query)
        self.connection.commit()

    def update_person_salary(self, salary, employee_id):
        """
        desc: updating employee details in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        query = "update employee_details set salary = %d where employee_id = %d " % (salary, employee_id)
        self.my_cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_employee_data(employee_id)
        return updated_data

    def update_employee_profile_image(self, profile_image, employee_id):
        """
        desc: updating employee profile image in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        query = "update employee_details set profile_image = '%s' where employee_id = %d" % (profile_image,
                                                                                             employee_id)
        self.my_cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_employee_data(employee_id)
        return updated_data

    def update_employee_name(self, employee_name, employee_id):
        """
        desc: updating employee name in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        query = "update employee_details set Employee_name = '%s' where employee_id = %d" % (employee_name,
                                                                                             employee_id)
        self.my_cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_employee_data(employee_id)
        return updated_data

    def update_employee_department(self, employee_department, employee_id):
        """
        desc: updating employee name in  the employee_details table
        param: salary, employee_name
        return: updated data or error
        """
        query = "update employee_details set department = '%s' where employee_id = %d" % (employee_department,
                                                                                          employee_id)
        self.my_cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_employee_data(employee_id)
        return updated_data

    def update_employee_gender(self, employee_gender, employee_id):
        """
        desc: updating employee gender in  the employee_details table
        param: gender, employee_name
        return: updated data or error
        """
        query = "update employee_details set employee_gender = '%s' where employee_id = %d" % (employee_gender,
                                                                                               employee_id)
        self.my_cursor.execute(query)
        self.connection.commit()
        updated_data = self.show_employee_data(employee_id)
        return updated_data

    def delete_person_by_id(self, employee_id):
        """
        desc: deleting employee details in  the employee_details table
        param: employee_name
        return: employee_id
        """
        self.show_employee_data(employee_id)
        query = "delete from employee_details where employee_id = %d" % employee_id
        self.my_cursor.execute(query)
        self.connection.commit()
