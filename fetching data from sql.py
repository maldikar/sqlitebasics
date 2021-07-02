import sqlite3

first_name = input('enter data: ')
last_name = input('enter data: ')
email = input('enter data: ')

conn = sqlite3.connect('customer.db')


#create cursor
c = conn.cursor()



#create list of multile entries
many_customer = [first_name,last_name,email]
                 
                 

#write into tables the'?' entered in the place of values is the placeholder 
#to insert variables in database write names of the columns in the table and write variables in paranthesis after sql command
c.execute("INSERT INTO customers (first_name,last_name,email) VALUES (?,?,?)", (first_name,last_name,email))




#commit our database
conn.commit()

#close our connection
conn.close()
