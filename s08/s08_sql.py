import sqlite3
from tkinter.messagebox import NO

def get_user(username):
    database_address = 'data.sqlite3'
    with sqlite3.connect(database_address) as con:
        cursor = con.cursor()
        result = cursor.execute(
            'select * from user where username=?',  (username,))
        users = result.fetchall()
        if users:
            return users
        else:
            return None

def set_user(username, password):
    database_address = 'data.sqlite3'
    with sqlite3.connect(database_address) as con:
        cursor = con.cursor()
        result = cursor.execute(
            'insert into user (username,password) values (?,?)',  (username, password))
        con.commit()
        return True

def register(username, password):
    if get_user(username):
        return False
    else:
        return set_user(username, password)

print(get_user('mohammad23'))
print(register('mohammad23', '2323'))
