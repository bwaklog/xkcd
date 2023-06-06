import mysql.connector as sql
import main.py as main

db = sql.connect(
    host="localhost",
    user="root",
    password="1029Adity@",
    database="xkcd",
)
cur = db.cursor()


def simple_read():
    print("Simple Reader!")
    cur.execute("use xkcd")
    cur.execute("select * from comics")
    print(cur.fetchall())

def writer(comic: main.Comic):
    pass


if __name__ == "__main__":
    simple_read()