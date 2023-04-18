# Name: Wenjia Hu

# Lab 6
import pandas as pd

# 1. Download the file 'mydata.csv' from Canvas. Load it into a DataFrame named mydata.
mydata = pd.read_csv('mydata.csv')
print(mydata)

# 2. Create t1 as just the entries of mydata that don't contain NaN values.
t1 = mydata.dropna()
print(t1)

# 3. Compute the average weight and the average age from t1.
avg_weight = t1['Weight'].mean()
ave_age = t1['Age'].mean()
print(avg_weight)
print(ave_age)

#4. Create t2 from mydata with the NaN fields in the Weight column replaced by the average weight. 
t2 = mydata.fillna({'Weight':avg_weight})
print(t2)

#5. Create t3 from mydata with the NaN fields in the Age column replaced by the average age.
t3 = mydata.fillna({'Age':ave_age})
print(t3)

# 6. Create t4 from t2 by doing #5 to replace missing Age values with the average age.
t4 = t2.fillna({'Age':ave_age})
print(t4)

# 7. Create t5 from mydata by forward-filling missing data.
t5 = mydata.fillna(method='ffill')
print(t5)

# 8. Create t6 as a copy t4. Then replace any Age values larger than 18 with the average age.
t6 = t4.copy()
t6.loc[t6['Age'] > 18, 'Age'] = ave_age
print(t6)

# 9. Create t7 as a copy of t6. Then replace any Weight values larger than 150 with the average weight.
t7 = t6.copy()
t7.loc[t7['Weight'] > 150, 'Weight'] = avg_weight
print(t7)

# 10. Create t8 from t7, changing its Age data to int (use astype() )
t8 = t7.astype({'Age':int})
print(t8)

#11. Create t9 from t8, changing any missing Name data to 'Barfy' using fillna( ). 
# Then use apply( ) to change the name column to upper case. Then change the Name column to 'Search Name'
t9 = t8.fillna({'Name':'Barfy'})
t9['Name'] = t9['Name'].apply(lambda x: x.upper())
t9 = t9.rename(columns={'Name':'Search Name'})
print(t9)

#12. Create t10 from t9 using pd.concat( ) and axis = 1, concatenating t9's Search Name column with all of t8.
t10 = pd.concat([t9['Search Name'], t8], axis=1)
print(t10)

# Lab 7

import sqlite3  as sql

# problem 1 
connection = sql.connect('dogsdb.sqlite3')
cursor = connection.cursor()
query='select name from sqlite_master where type="table"' 
cursor.execute(query)
table = cursor.fetchall()
print(table)


# problem 2

#Create a query string to get all the data from dogs. 
# Execute the query into 'cursor', use it to get all the data into a variable named table, 
# and display table and its type. Then loop over table and display its rows.

query = 'select * from dogs'
cursor.execute(query)
table = cursor.fetchall()
print(table)
print(type(table))
for row in table:
    print(row)


#3. Display cursor.description. 
# Iterate over it to show just the column names (position 0). 
# Create an empty list named colnames. 
# Then do the iteration again and append those names to colnames. 
# Display colnames; it should be a list of the str names of the columns of dogsdb.sqlite3.

print(cursor.description)
for row in cursor.description:
    print(row[0])

colnames = []
for row in cursor.description:
    colnames.append(row[0])

print(colnames)


#4. Create a pandas DataFrame named dogsDF with table as the data and colnames as the columns. Display it.
dogsDF = pd.DataFrame(table, columns=colnames)
print(dogsDF)

#5. Download the file 'breeds.py' from Canvas; it contains a list of lists named 'breeds'. 
# Copy it into your interpreter; display breeds. No real work here – just saving you some typing (you're welcome).
import breeds
print(breeds.breeds)

#6. Create a new table in dogdb named Breeds with the column names Breed, VARCHAR(20), and Description, VARCHAR(40). 
# Then insert the data from breeds in #5 into it.

cursor.execute('''CREATE TABLE Breeds (
                Breed VARCHAR(20),
                Description VARCHAR(40)
              )''')

for row in breeds.breeds:
    cursor.execute('''INSERT INTO Breeds VALUES (?,?)''', row)
connection.commit()

#7. Query the table Breeds from dogdb and display it (i.e., as proof that it was stored).
query = 'select * from Breeds'
cursor.execute(query)
table = cursor.fetchall()
print(table)

# 8. Write a JOIN query to join dogs with Breeds on the Breed field, but limited to the Name, Breed, and Description fields.

query = '''SELECT dogs.Name, dogs.Breed, Breeds.Description
            FROM dogs
            JOIN Breeds
            ON dogs.Breed = Breeds.Breed'''
cursor.execute(query)
table = cursor.fetchall()
print(table)

#9. Write a SELECT query to get dogs at least 5 years old. Display their names and ages only.
query = '''SELECT Name, Age
            FROM dogs
            WHERE Age >= 5'''
cursor.execute(query)
table = cursor.fetchall()
print(table)

# 10. Write a SELECT query to get the average age (use AVG(dogs.Age) ) 
# display it in a formatted Python statement with a label and 2 decimal places.

query = '''SELECT AVG(Age)
            FROM dogs'''
cursor.execute(query)
table = cursor.fetchall()
print(table)
print('The average age of the dogs is {:.2f}'.format(table[0][0]))
