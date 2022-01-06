"""
@author: Dibyesh Mishra
@date: 03-01-2022 01:31
"""
from pydantic import BaseModel


class Employee(BaseModel):
    """
    this class contains attributes related to employee details
    """
    employee_id : int
    employee_name: str
    profile_image: str
    employee_gender: str
    department: str
    salary: int
    start_date: str
    notes: str
