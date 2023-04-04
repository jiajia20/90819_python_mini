
#Open the database named 'LeeBooks.db' and get its cursor. 
import sqlite3
import pandas as pd
# 3a
# 3a.1
# Connect to the database
conn = sqlite3.connect('LeeBooks.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')

# Fetch the results and print them
print('Table list:')
rows = cursor.fetchall()
for i in range(len(rows)):
     print(rows[i][0])

## 3a.2
cursor.execute('SELECT COUNT(*) FROM' + rows[0][0])
results = cursor.fetchone()
print('# rows = ', results[0])


## 3a.3
cursor.execute('PRAGMA table_info(' + rows[0][0] + ')')
results = cursor.fetchall()

print('Column list:')
for i in range(len(results)):
    print(results[i][1], end='\n')

# Close the connection
conn.close()


# 3b
# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
sql_query= 'SELECT LASTNAME, FIRSTNAME, STATE FROM CUSTOMERS'

df = pd.read_sql_query(sql_query, conn)

#closes the connection
conn.close()

#select LASTNAEM, FIRSTNAME, STATE from CUSTOMERS
#df = df[['LASTNAME', 'FIRSTNAME', 'STATE']]

#Then sort it on the STATE field and display that. 
df.sort_values(by=['STATE'])


# Then sort it by both STATE and LASTNAME (put them in [ ] as the parameter to sort_values( )).
df.sort_values(by=['STATE', 'LASTNAME'])

# 3c
#Create a DataFrame called orderItemsDF from the ORDERITEMS table, 
# using just the ORDERNUM, QUANTITY, and PAIDEACH fields. 

# create pandas dataframe from databse
conn = sqlite3.connect('LeeBooks.db')
cursor = conn.cursor()
sql_query= 'SELECT ORDERNUM, QUANTITY, PAIDEACH FROM ORDERITEMS'

#sql_query= 'SELECT * FROM ORDERITEMS'
df = pd.read_sql_query(sql_query, conn)

#closes the connection
conn.close()

# Make sure it has those column names. Display it. 
print(df)
# Add a new column, TOTAL, which is the QUANTITY field times the PAIDEACH field.
df['TOTAL'] = df['QUANTITY'] * df['PAIDEACH']
#  
# Display the table.  
print(df)
# Then use it to compute the overall TOTAL and display that as a money value with a label.
print('Total: $', df['TOTAL'].sum())


## 3d
#Use the syntax CREATE TABLE <newtable> AS <some SELECT query> to create a new db table called BOOKLIST,
#  where the SELECT query is a join of BOOKS and BOOKAUTHOR on ISBN joined to AUTHOR on AUTHORID,
#  keeping only the author's LNAME and FNAME and the book's TITLE. 

# To display this table, execute the query SELECT * FROM BOOKLIST and fetch the tuples.

conn = sqlite3.connect('LeeBooks.db')
cursor = conn.cursor()

sql_query1= 'SELECT ISBN, TITLE FROM BOOKS'
df1 = pd.read_sql_query(sql_query1, conn)

sql_query2= 'SELECT AUTHORID, LNAME, FNAME FROM AUTHOR'
df2 = pd.read_sql_query(sql_query2, conn)

sql_query3= 'SELECT ISBN, AUTHORID FROM BOOKAUTHOR'
df3 = pd.read_sql_query(sql_query3, conn)

#join df1 to df3
df3 = pd.merge(df1, df3, on='ISBN')
#join df2 to df3
df3 = pd.merge(df2, df3, on='AUTHORID')
df3.to_sql('BOOKLIST', conn, if_exists='replace', index = False)

# load BOOKLIST table
sql_query1= 'SELECT * FROM BOOKLIST'
bookListDF  = pd.read_sql_query(sql_query1, conn)

conn.close()


## 3e
#Display bookListDF.
print(bookListDF) 
# Sort bookListDF on LNAME, FNAME (see the hint in part b) and display it again. 
bookListDF.sort_values(by=['LNAME', 'FNAME'])

# Group the dataframe by LNAME, 
bookListDF = bookListDF.groupby('LNAME')



# select that column, and count( ) the entries – display the result. 
print(bookListDF)
# What's wrong  with these counts? No need to answer that in the code, but you should think about it.
Can'