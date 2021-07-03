import sqlite3




connection = sqlite3.connect('store_database.db')

cursor = connection.cursor()
    
#create stores tables
    
 

cursor.execute("""CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)""")


#create a purchase table



cursor.execute( """CREATE TABLE IF NOT EXISTS
purchases(purshase_id INTEGER PRIMARY KEY,store_id INTEGER , total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))""")


#add to stores

cursor.execute("INSERT INTO stores VALUES( 1,'DOMBIVLI')")
cursor.execute("INSERT INTO stores VALUES( 3,'DOMBIVLI')")
cursor.execute("INSERT INTO stores VALUES( 2,'DOMBIVLI')")

#add to purchases

cursor.execute("INSERT INTO purchases VALUES( 231, 1 ,33.25)")
cursor.execute("INSERT INTO purchases VALUES( 21, 2 ,363.25)")
cursor.execute("INSERT INTO purchases VALUES( 23, 3 ,335.25)")

#get result
cursor.execute("SELECT * FROM purchases")
results = cursor.fetchall()
print(results)

cursor.execute("SELECT * FROM stores")
data = cursor.fetchall()
print(data)
