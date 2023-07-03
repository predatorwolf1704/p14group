import sqlite3


class DB:
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    post_table = """
        create table if not exists posts(
            id integer primary key autoincrement,
            title varchar(300),
            description text,
            created_at timestamp default current_timestamp   
        );
    """
    comment_table = """
            create table if not exists comment(
                id integer primary key autoincrement,
                message text,
                created_at timestamp default current_timestamp   
            );
        """
    cur.execute(post_table)
    cur.execute(comment_table)
    con.commit()


    def select(self , **kwargs):
        if self.fields:
            fields = ",".join(self.fields)
        else:
            fields = '*'

        if kwargs:
            where_keys = "where " + " = ? and ".join(kwargs.keys()) + " = ?"
        else:
            where_keys = ""

        table_name = self.__class__.__name__.lower()
        query = """select {} from {} {}""".format(fields , table_name, where_keys)
        self.cur.execute(query , tuple(kwargs.values()))
        return self.cur.fetchall()


    def insert(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass




