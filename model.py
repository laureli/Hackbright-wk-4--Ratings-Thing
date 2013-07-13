import sqlite3
import shlex

DB=None
CONN=None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("rates.db")
    DB = CONN.cursor()

class User(object):
    def __init__(self, idnum, name, email, password):
        self.idnum = idnum
        self.name = name
        self.email = email
        self.password = password

    def get_posts_user(self):
        sql = """select Posts.id, Posts.title, Posts.body,
                Posts.category, Posts.created_at, Rates.value
                from Posts
                inner join Rates on Posts.user_id = Rates.user_id
                where Posts.user_id=?"""
        DB.execute(sql, (self.idnum,))
        posts = DB.fetchall()

        p_list = []
        for p in posts:
            p = Posts(p[0], p[1], p[2], p[3], p[4], p[5])
            p_list.append(p)

        return p_list


class Posts(object):
    def __init__(self, idnum, title, body, category, created_at, value):
        self.idnum = idnum
        self.title = title
        self.body = body
        self.category = category
        self.created_at = created_at
        self.value = value 


def get_user(idnum):
    sql = "select name, email, password from Users where id=?"
    DB.execute(sql, (idnum,))
    row = DB.fetchone()
    u = User(idnum, row[0], row[1], row[2])
    return u

def login(name, password):
    sql = "select id, name, email, password from Users where name=? AND password=?"
    DB.execute(sql, (name, password))
    row = DB.fetchone()
    print "This is a row:", row
    try:
        u = User(row[0], row[1], row[2], row[3])
        return u
    except TypeError:
        return "NO"
