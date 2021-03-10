"""
First create a wrapper for the API Provided
"""

import requests


class ApiWrapper:
    def __init__(self):
        self.host_ip = "http://34.240.242.168:7001/"

    def get_all_bears(self):
        return requests.get(self.host_ip + "/bear").json()

    def get_a_bear(self, id):
        return requests.get(self.host_ip + f"/bear/{id}").json()

    def delete_all_bears(self):
        return requests.delete(self.host_ip + "/bear").status_code

    def delete_a_bear(self, id):
        return requests.delete(self.host_ip + f"/bear/{id}").status_code

    def add_a_bear(self, bear_type, name, description, age, mother_number=None):
        data = {"bear_type": bear_type,
                "name": name,
                "description": description,
                "age": age}
        if mother_number is not None:
            data["mother_number"] = mother_number

        return requests.post(self.host_ip + "/bear", json=data).status_code

    def update_a_bear(self, id, bear_type, name, description, age, mother_number=None):
        data = {"bear_type": bear_type,
                "name": name,
                "description": description,
                "age": age}
        if mother_number is not None:
            data["mother_number"] = mother_number
        return requests.put(self.host_ip + f"/bear/{id}", json=data).status_code

