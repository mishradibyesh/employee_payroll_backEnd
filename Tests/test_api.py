"""
@author: Dibyesh Mishra
@date: 06-01-2022 08:01
"""
import pytest

from main import app
from fastapi.testclient import TestClient
client = TestClient(app)


class TestForApi:
    @pytest.mark.parametrize('table_name', ["employee_details"])
    def test_all_data_in_table(self, table_name):
        response = client.get(f"/get_table/{table_name}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully retrieved  Employee Details table"

    @pytest.mark.parametrize('table_name', ["detail"])
    def test_if_table_is_not_present_in_db(self, table_name):
        response = client.get(f"/get_table/{table_name}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : 1146 (42S02): Table 'employee_payroll.detail' doesn't exist"

    @pytest.mark.parametrize('employee_id', [2])
    def test_employee_data(self, employee_id):
        response = client.get(f"/get_data_by_id/{employee_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully retrieved  Employee Details table"

    @pytest.mark.parametrize('employee_id', [2999])
    def test_table_data_if_wrong_id(self, employee_id):
        response = client.get(f"/get_data_by_id/{employee_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : this id is not present in the database"

    @pytest.mark.parametrize('employee_id', ["ssds"])
    def test_table_data_if_wrong_format_of_id_provided(self, employee_id):
        response = client.get(f"/get_data_by_id/{employee_id}")
        assert response.status_code == 422
        assert response.json()["detail"][0]["msg"] == "value is not a valid integer"

    @pytest.mark.parametrize('employee_data', [
        {"employee_id": 18832, "employee_name": "string", "profile_image": "string", "employee_gender": "string",
            "department": "string", "salary": 2222222, "start_date": "2023-02-02", "notes": "string"}])
    def test_if_employee_added_to_db(self, employee_data):
        response = client.post("/add_employee/", json=employee_data)
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully added The Employee Details"

    @pytest.mark.parametrize('employee_id , salary', [(2, 23333)])
    def test_if_salary_is_updated_in_database(self, employee_id, salary):
        response = client.put(f"/update_person_salary/{employee_id}/{salary}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully updated the Employee Details"

    @pytest.mark.parametrize('employee_id , salary', [(2323, 23333)])
    def test_if_salary_is_not_updated_in_database_due_to_wrong_id(self, employee_id, salary):
        response = client.put(f"/update_person_salary/{employee_id}/{salary}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : this id is not present in the database"

    @pytest.mark.parametrize('employee_id , profile_image', [(2, 'image.jpg')])
    def test_if_salary_is_updated_in_database(self, employee_id, profile_image):
        response = client.put(f"/update_person_profile_img/{employee_id}/{profile_image}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully updated the Employee Details"

    @pytest.mark.parametrize('employee_id , profile_image', [(2777, 'image.jpg')])
    def test_if_profile_image_is_not_updated_in_database_due_to_wrong_id(self, employee_id, profile_image):
        response = client.put(f"/update_person_profile_img/{employee_id}/{profile_image}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : this id is not present in the database"

    @pytest.mark.parametrize('employee_id , department', [(2, 'Engineer')])
    def test_if_department_is_updated_in_database(self, employee_id, department):
        response = client.put(f"/update_person_department/{employee_id}/{department}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully updated the Employee Details"

    @pytest.mark.parametrize('employee_id , profile_image', [(244, 'image.jpg')])
    def test_if_department_is_not_updated_in_database_due_to_wrong_id(self, employee_id, profile_image):
        response = client.put(f"/update_person_profile_img/{employee_id}/{profile_image}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : this id is not present in the database"

    @pytest.mark.parametrize('employee_id', [(12232)])
    def test_if_employee_id_is_deleted_from_database(self, employee_id):
        response = client.delete(f"/delete_person_by_id/{employee_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Successfully deleted one Employee Details"

    @pytest.mark.parametrize('employee_id', [(222221)])
    def test_if_employee_id_is_not_deleted_from_database(self, employee_id):
        response = client.delete(f"/delete_person_by_id/{employee_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Error : this id is not present in the database"

    def test_if_login_is_successful(self):
        response = client.post(f"/employee_login", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NzgxfQ.Ub85UWCtE80oVMLG6Y4-5oGJkZROu_udkvzz7l8gHek"})
        assert response.json()['message'] == "successfully logged in"

    def test_if_login_is_unsuccessful(self):
        response = client.post(f"/employee_login", headers={
            "token": "easyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NzgxfQ.Ub85UWCtE80oVMLG6Y4-"
                     "5oGJkZROu_udkvzz7l8gHek"})
        assert response.json()['message'] == "Error : Invalid header string: 'utf-8' codec can't decode" \
                                             " byte 0xab in position 1: invalid start byte"
