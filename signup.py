# File to signup new user

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ALICE")

my_cursor = mydb.cursor()


def sign_up():

    name = input("Enter your name: ")
    username = input("Enter your desired username: ")
    password = input("Enter your password: ")

    my_cursor.execute("INSERT INTO login_info(name, UserID, Password) VALUES (%s, %s, %s)", (name, username, password))

    mydb.commit()
    print("Data inserted successfully")
