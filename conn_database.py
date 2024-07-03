# File to create database in MySQL

# Import the MySQL connector module
import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",  # MySQL server hostname
    user="root",       # MySQL username
    password="root",   # MySQL password
)

try:
    # Create a cursor object to execute SQL queries
    my_cursor = mydb.cursor()

    # Execute SQL query to create a database named "ALICE" if it does not exist
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS ALICE")

    # Commit the transaction
    mydb.commit()

    # Print a message indicating successful creation of the database
    print("Database created")
except Exception as e:
    # Handle exceptions and print error message if any
    print(e)
    print("Error Occurred")
