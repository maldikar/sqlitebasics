import sqlite3


conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS userdata(username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, email_address VARCHAR NOT NULL, contact_no VARCHAR NOT NULL)""")
    
    # taking inputs from the user
    un = input('Enter username:' )
    pa = input('Enter password:' )
    ea = input('Enter email address:' )
    cn = input('Enter contact no:' )
    
    #checking if username entered already exists and it it does taking another input
    c.execute("SELECT 1 FROM userdata WHERE username=?", (un,))
    while len(c.fetchall()) > 0:
        print('Username already exists, please try again')
        un = input('Enter username:' )
        pa = input('Enter password:' )
        c.execute("SELECT 1 FROM userdata WHERE username=?", (un,))