import sqlite3
import os

SEPARATOR = "/" if os.name != "nt" else "\\"

appdata = f"{os.getenv('PROGRAMDATA')}\\soft" if os.name == 'nt' else "/opt/soft"

try:
    DB = sqlite3.connect(f"{appdata}{SEPARATOR}data.db", check_same_thread=False)
except:
    open(f"{appdata}{SEPARATOR}data.db", "w").close()
    DB = sqlite3.connect(f"{appdata}{SEPARATOR}data.db",  check_same_thread=False)

def check_if_user_exists(username):
    con = DB.cursor()
    con = con.execute(f"SELECT 1 FROM users WHERE username='{username}'")
    return True if con.fetchone() else False

def get_username():
    name = input("Enter a username [user]: ")
    if name == "":
        name = "user"
    return name

def get_username_not_mandatory():
    name = input("Enter a username: ")
    if name == "":
        return None
    return name

def pull_password(username):
    con = DB.cursor()
    con = con.execute(f"SELECT password FROM users WHERE username='{username}'")
    return con.fetchone()[0]

def get_password(username):
    password = input(f"Enter a password for {username}: ")
    if password == "":
        print("Password cannot be empty!")
        get_password(username)
    con = DB.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    con.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
    DB.commit()
    del password