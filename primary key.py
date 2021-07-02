import sqlite3


conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor()


#fetch data
#Sqlite database gives an id number to every row which can be seen and used by using "SELECT rowid, * FROM customers".
c.execute("SELECT rowid, * FROM customers")


data = c.fetchall()
for item in data:
    print(item)
    

#commit our database
conn.commit()

#close our connection
conn.close()

#output
#(1, 'mohit', 'maldikar', 'mohitmaldikar@gmail.com')
#(2, 'mohit', 'maldikar', 'mohitmaldikar@gmail.com')
#(3, 'moh', 'maldik', 'mohitmaldar@gmail.com')
#(4, 'moh', 'maldik', 'mohitmaldar@gmail.com')
#(5, 'mgolu', 'dfdgk', 'ghdhf')
#(6, 'mgolu', 'dfdgk', 'ghdhf')
#(7, 'mgolu', 'dfdgk', 'ghdf')
#(8, 'mgolu', 'dfdgk', 'ghgjf')
#(9, 'xfg', 'xbh', 'xsh')