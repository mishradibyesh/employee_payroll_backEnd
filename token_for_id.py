"""
@author: Dibyesh Mishra
@date: 05-01-2022 20:12
"""
import jwt


class TokenForLogin:
    """
    this class has methods which have functionalities like encode and decode
    """
    def encode_id(self, employee_id):
        """
        desc: encoding the employee_id
        param: employee_id:
        return: generated_token
        """
        payload = {"id": employee_id}
        token_generated = jwt.encode(payload, "secret_code")
        return token_generated

    def decode_id(self, token_id):
        """
        desc: decoding the employee_id
        param: employee_id:
        return: decoded employee id
        """
        payload = jwt.decode(token_id, "secret_code", algorithms=["HS256"])
        return payload.get('id')