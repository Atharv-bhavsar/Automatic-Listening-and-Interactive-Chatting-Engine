from tkinter import *
from tkinter import messagebox
import mysql.connector

def startLogin():
    # Establish connection with MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ALICE"
    )

    root = Tk()
    root.title("Login")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 900  # set your desired window width
    window_height = 500  # set your desired window height
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    print(x, y)
    root.overrideredirect(True)
    root.config(bg='#fff')
    # root.iconbitmap('alice_logo.ico')
    root.resizable(False, False)


    def signup_command(event=None):

        window = Toplevel(root)
        window.title("SignUp")
        window.geometry('925x500+318+182')
        window.configure(bg='#fff')
        window.resizable(False, False)
        window.iconbitmap('Images/alice_logo.ico')
        window.overrideredirect(True)

        def signup(event=None):
            realname = name.get()
            username = user.get()
            password = code.get()

            # No input is given
            if realname == 'Name' and username == "Username" and password == 'Password':
                temp = Toplevel()


                def closeTemp():
                    temp.destroy()

                temp.title("Error")
                temp.geometry('400x200+450+250')
                tempLabel = Label(temp, text="Enter All Credentials", fg='red', font=("Arial", 23, "bold"))
                tempLabel.place(x=60, y=10)
                tempButton = Button(temp, text='  Ok  ', bg='red', fg='white', font="Arial", command=closeTemp)
                tempButton.place(x=180, y=80)
                temp.mainloop()


            # One of the credentials isn't given
            if (realname == 'Name' or username == "Username" or password == 'Password'):
                temp = Toplevel()

                def closeTemp():
                    temp.destroy()

                temp.title("Error")
                temp.geometry('400x200+450+250')
                tempLabel = Label(temp, text="Enter All Credentials", fg='red', font=("Arial", 23, "bold"))
                tempLabel.place(x=60, y=10)
                tempButton = Button(temp, text='  Ok  ', bg='red', fg='white', font="Arial", command=closeTemp)
                tempButton.place(x=180, y=80)
                temp.mainloop()

            # Successful sign up
            else:
                # Execute the SQL query to insert new user data into the database
                my_cursor = mydb.cursor()
                my_cursor.execute("INSERT INTO login_info(name, UserID, Password) VALUES (%s, %s, %s)",
                                  (realname, username, password))


                # Commit the transaction
                mydb.commit()
                window.destroy()
                root.destroy()

        img = PhotoImage(file='Images/signup.png')
        Label(window, image=img, border=0, bg='white').place(x=50, y=90)
        frame = Frame(window, width=350, height=390, bg='#fff')
        frame.place(x=480, y=50)

        heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=100, y=5)

        ################__________________________#############

        def on_enter(e):
            name.delete(0, 'end')

        def on_leave(e):
            if name.get() == '':
                name.insert(0, 'Name')

        name = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        name.place(x=30, y=91)
        name.insert(0, 'Name')
        name.bind("<FocusIn>", on_enter)
        name.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=117)

        # --------------------
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Username')

        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        user.place(x=30, y=145)
        user.insert(0, 'Username')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=172)

        ################__________________________#############

        code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))


        def on_enter(e):
            code.delete(0, 'end')
            code.config(show='*')

        def on_leave(e):
            if code.get() == '':
                code.insert(0, 'Password')
        code.place(x=30, y=200)
        code.insert(0, 'Password')
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=227)

        ################__________________________####################

        Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,
                                                                                                                  y=280)
        root.bind("<Return>", signup)
        window.mainloop()
        root.destroy()


    def show_invalid_credentials_error():
        temp = Toplevel()
        temp.title("Error")
        temp.geometry('400x200+450+250')
        tempLabel = Label(temp, text="Invalid Credentials", fg='red', font=("Arial", 23, "bold"))
        tempLabel.place(x=60, y=10)
        tempButton = Button(temp, text='  Ok  ', bg='red', fg='white', font="Arial", command=temp.destroy)
        tempButton.place(x=180, y=80)
        temp.mainloop()

    def login(username, password):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="ALICE"
            )
            # Create a cursor object to execute queries
            mycursor = mydb.cursor()
            # Execute a query to check if the username and password match
            mycursor.execute("SELECT * FROM login_info WHERE UserID = %s AND Password = %s", (username, password))
            # Fetch one row from the result
            my_result = mycursor.fetchall()
            # If a user with the provided username and password exists, return True
            if my_result:
                root.destroy()
                return True
            else:
                show_invalid_credentials_error()
                # return False
        except mysql.connector.Error as error:
            print("Error connecting to MySQL database:", error)
            return False

    img = PhotoImage(file='Images/login.png')
    label0 = Label(root, image=img, bg='white')
    label0.place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Log in", fg='#57a1f8', bg='white', font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    #####################--------------------------------#######################

    def on_entry(e):
        name.delete(0, 'end')

    def on_leave(e):
        realname = name.get()
        if realname == '':
            name.insert(0, 'Username')

    name = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11, "bold"))
    name.place(x=30, y=90)
    name.insert(0, 'Username')
    name.bind('<FocusIn>', on_entry)
    name.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=115)

    # ---------------------------------------------------------------------------------------------------------- #

    password = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11, "bold"))

    def on_entry(e):
        password.delete(0, 'end')
        password.config(show='*')

    def on_leave(e):
        name = password.get()
        if name == '':
            password.insert(0, 'Password')
    password.place(x=30, y=150)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_entry)
    password.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=173)
    # ------------------------------------------------------------------------------------------------- #
    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                     command=signup_command)
    sign_up.place(x=255, y=272)

    login_result = BooleanVar()

    def check_login(event=None):
        login_result.set(login(name.get(), password.get()))

    Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8', fg='white', border=0, command=check_login).place(x=35, y=204)
    root.bind("<Return>", check_login)

    label = Label(frame, text="Don't have an account?", fg='black', bg='white',
                  font=("Microsoft YaHei UI Light", 11, "bold"))
    label.place(x=55, y=270)

    root.mainloop()

    return login_result.get()


startLogin()