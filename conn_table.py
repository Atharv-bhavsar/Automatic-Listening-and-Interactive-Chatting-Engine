# File to create tables in ALICE database

# Import the MySQL connector module
import mysql.connector

# Connect to MySQL server and select the ALICE database
mydb = mysql.connector.connect(
    host="localhost",   # MySQL server hostname
    user="root",        # MySQL username
    password="root",    # MySQL password
    database="ALICE"    # Database name
)

try:
    # Create a cursor object to execute SQL queries
    my_cursor = mydb.cursor()

    # Execute SQL query to create a table named "login_info" if it does not exist
    my_cursor.execute("CREATE TABLE IF NOT EXISTS login_info (Name VARCHAR(50), UserID VARCHAR(50),"
                      "Password VARCHAR(50))")

    # Define SQL query to insert records into the table
    sql = "INSERT INTO login_info (Name, UserID, Password) VALUES (%s, %s, %s)"

    # Define values to be inserted into the table
    val = [
        ("Rafan", "rafzz", "438"),
        ("Aditya", "aditya", "431"),
        ("Mehul", "mehul", "427"),
        ("Arfan", "arfan", "445")
    ]

    # Execute SQL query to insert multiple records into the table
    my_cursor.executemany(sql, val)

    # Commit the transaction
    mydb.commit()

    # Print the number of records inserted
    print(my_cursor.rowcount, "Records inserted.")
except Exception as e:
    # Handle exceptions and print error message if any
    print(e)
    print("Error occurred")
