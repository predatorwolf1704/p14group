import sqlite3

class DB:
    con = sqlite3.connect("parking_db.sqlite")
    cur = con.cursor()

    query1 = """
    create table if not exists users(
        id integer primary key autoincrement,
        name varchar(255) not null,
        username varchar(30) unique,
        password varchar(10),
        created_at date default current_date 
    );
    -- primary key(not null , unique, created index)
    """
    # query2 = """
    # create table if not exists cars(
    #     id integer primary key autoincrement,
    #     user_id integer,
    #     model varchar(255) not null,
    #     number varchar(255) not null,
    #      varchar(255) not null,
    #     created_at timestamp default current_timestamp
    # );
    cur.execute(query1)
    con.commit()
    

    
