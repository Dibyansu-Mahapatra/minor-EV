
import sqlite3


con=sqlite3.connect('user1.db')
c=con.cursor()

command="""CREATE TABLE IF NOT EXISTS users(name TEXT, email TEXT, password TEXT)"""
c.execute(command)

c.execute("INSERT INTO users VALUES('Jiggi','jiggi@gmail.com','jiggii')")

con.commit()