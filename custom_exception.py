"""
@author: Dibyesh Mishra
@date: 04-01-2022 07:31
"""


class DataNotFound(Exception):
    """
    defining custom exception
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message