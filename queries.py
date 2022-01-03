"""
@author: Dibyesh Mishra
@date: 02-01-2022 19:49
"""
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
        query = "select * from employee_details"
        self.my_cursor.execute(query)
        data_list = []
        for i in self.my_cursor:
            data_list.append(i)
        return data_list

    def add_employee_db(self,employee_name, profile_image, employee_gender, department, salary, start_date, notes):
        """
        desc: adding employee details in  the employee_details table
        param : employee_name, profile_image, employee_gender, department, salary, start_date, notes
        return: message string
        """
        query = "insert into employee_details (employee_name, profile_image, employee_gender, department, salary," \
                " start_date, notes) values ('%s', '%s', '%s', '%s', %d, '%s', '%s')" % (
                  employee_name, profile_image, employee_gender, department, salary, start_date, notes)
        self.my_cursor.execute(query)
        self.connection.commit()

    def update_person_details(self,salary, employee_name):
        """
        desc: updating employee details in  the employee_details table
        param: salary, employee_name
        return: message string
        """
        query = "update employee_details set salary = %d where employee_name = '%s' " % (salary, employee_name)
        self.my_cursor.execute(query)
        self.connection.commit()

    def delete_person_by_name(self,employee_name):
        """
        desc: deleting employee details in  the employee_details table
        param: employee_name
        return: message string
        """
        query = "delete from employee_details where employee_name = '%s'" % employee_name
        self.my_cursor.execute(query)
        self.connection.commit()
