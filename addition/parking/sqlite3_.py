# file ko'rinishidagi database
# json -> 1_000_000

import sqlite3

con = sqlite3.connect('../test.sqlite')
cur = con.cursor()

query1 = """
create table if not exists post(
    id integer primary key autoincrement,
    title varchar(255) not null,
    description text,
    created_at date default current_date 
);
-- primary key(not null , unique, created index)
"""
query2 = """
create table if not exists comment(
    id integer primary key autoincrement,
    post_id integer,
    message varchar(255) not null,
    created_at timestamp default current_timestamp 
);
"""

cur.execute(query1)
cur.execute(query2)
con.commit()





