from dataclasses import dataclass

from addition.UnversalDB.db import DB



class Posts(DB):
    def __init__(self , *fields):
        self.fields = fields   # ("id", "title")


class Comment(DB):
    def __init__(self , *fields):
        self.fields = fields


print(Posts().select(id =1))
