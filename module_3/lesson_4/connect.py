import sqlite3


con = sqlite3.connect("/home/dilshod/PycharmProjects/p14_group/test.sqlite")
cur = con.cursor()


query = """insert into users(id , fullname , password) values(1 , 'Mahmud' , '1234')"""

cur.execute(query)
con.commit()


