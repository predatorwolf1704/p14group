import dataclasses
import json
import time
from dataclasses import dataclass


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        return data

    def write(self, data):
        with open(self.filepath, 'w') as f:
            json.dump(data, f , indent=3)


@dataclass
class User:
    fullname: str = None
    username: str = None
    password: str = None
    role: str = None
    email: str = None
    created_at: str = time.strftime("%Y-%m-%d %H:%M")

    def check_data(self):
        if not self.username:
            raise Exception("Username kiritilmagan")

        obj = File("db/users.json")
        data = obj.read()
        for i in data:
            if i['username'] == self.username:
                raise Exception("Bunday username ishlatilgan")

        if len(self.password) < 4:
            raise Exception("Password da xatolik EXAMPLE: 1234")

    def save_data(self):
        obj = File("db/users.json")
        data = obj.read()
        data.append(self.__dict__)
        obj.write(data)

    def login(self):
        obj = File("db/users.json")
        users = obj.read()
        for i in users:
            if i.get('username') == self.username and i.get('password') == self.password:
                return "Successfully login !"
        else:
            raise Exception("Invalid username or password !")














