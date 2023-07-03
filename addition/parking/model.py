from dataclasses import dataclass

from addition.parking.db import DB


@dataclass
class User(DB):
    id: int = None
    name: str = None
    username: str = None
    password: str = None

    def check_user(self):
        query = """select id from users where username = ?"""
        param = (self.username,)
        self.cur.execute(query , param)
        if self.cur.fetchone():
            return True



    def select_user(self):
        pass

    def save_user(self):
        query = """insert into users(name , username,password ) 
        values (? , ? , ?)"""
        params = (self.name , self.username , self.password)
        self.cur.execute(query , params)
        self.con.commit()


@dataclass
class Car:
    id = None
    model = None
    number = None
    color = None
    status = None











