import sqlite3


conn = sqlite3.connect('customer.db')


#create cursor
c = conn.cursor()

#create list of multile entries
many_customer = [('mgolu','dfdgk','ghdhf'),
                 ('mgolu','dfdgk','ghdhf'),
                 ('mgolu','dfdgk','ghdf'),
                 ('mgolu','dfdgk','ghgjf'),
                 ]

#write into tables the'?' entered in the place of values is the placeholder
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)


#commit our database
conn.commit()

#close our connection
conn.close()
