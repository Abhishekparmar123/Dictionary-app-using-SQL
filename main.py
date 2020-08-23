import sqlite3
import json

data = json.load(open("data.json"))


def create():
    conn = sqlite3.connect("Dictionary.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dictionary (word VARCHAR(30), meaning VARCHAR(1000))")
    conn.commit()
    conn.close()


def insert(word, meaning):
    conn = sqlite3.connect("Dictionary.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO dictionary VALUES (?, ?)", (word, meaning))
    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect("Dictionary.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM dictionary ")
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("Dictionary.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary ")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(item):
    conn = sqlite3.connect("Dictionary.db")
    cur = conn.cursor()
    cur.execute("SELECT meaning FROM dictionary WHERE word like ?", (item,))
    row = cur.fetchall()
    conn.close()
    return row


create()
key = list(data.keys())

# for i in key:
#    insert(i, str(data[i]))

# print(view())
# delete()
word = input("Enter your word : ")
result = (search(word))
result = list(result[0])
