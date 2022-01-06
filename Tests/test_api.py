"""
@author: Dibyesh Mishra
@date: 06-01-2022 08:01
"""
import pytest

from main import app
from fastapi.testclient import TestClient
client = TestClient(app)

class TestForApi:
    def test_table_data(self):
        response = client.get(f"get_table/employee_details")
        assert response.status_code == 200
        assert response.jason() == {
        "status": 200,
        "message": "Successfully retrieved  Employee Details table",
        "data": [
            [
                1,
                "Dibyesh",
                "abc.jpeg",
                "male",
                "IT",
                60000000,
                "2022-02-02",
                "hard working"
            ],
            [
                2,
                "GYANESH",
                "abcj.jpg",
                "male",
                "Finance,hr",
                334,
                "2022-02-02",
                "hard working"
            ],
            [
                3,
                "prashant",
                "absssccc.jpeg",
                "female",
                "Finance,hr",
                20000000,
                "2022-03-02",
                "hard working"
            ],
            [
                4,
                "abhay",
                "absssaaccc.jpeg",
                "male",
                "IT",
                45667,
                "2022-03-02",
                "hard working"
            ],
            [
                5,
                "akhshat",
                "absssaaccsssc.jpeg",
                "male",
                "IT",
                9999,
                "2021-03-02",
                "hard working"
            ],
            [
                7,
                "ramu",
                "ghh.jpg",
                "male",
                "HR, IT",
                222222,
                "2022-02-02",
                "good"
            ],
            [
                8,
                "jkjk",
                "absssasssassccsssc.jpeg",
                "female",
                "IT",
                45667,
                "2021-03-02",
                "hard working"
            ],
            [
                9,
                "arun",
                "ajdk.jpeg",
                "male",
                "finance",
                222222,
                "2022-03-03",
                "excellent"
            ],
            [
                10,
                "shyamu",
                "dffd.jpeg",
                "male",
                "finance,hr",
                22233222,
                "2022-03-03",
                "excellent employee"
            ],
            [
                1881,
                "shyamu",
                "dffd.jpeg",
                "male",
                "finance,hr",
                22233222,
                "2022-03-03",
                "excellent employee"
            ],
            [
                188221,
                "amu",
                "dffd.jpeg",
                "male",
                "finance,hr",
                22233222,
                "2022-03-03",
                "excellent employee"
            ]
        ]
        }