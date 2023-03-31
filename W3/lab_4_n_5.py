# Lab 4
# Problem 1

import pandas as pd

## 1.a
#create pandas series from list
a = pd.Series([i for i in range(5,1,-1)])
b = pd.Series([i for i in range(10,14)])
c = pd.Series([-1, -1, 0, 0])

## 1.b
print(a+b)
print(b-a)
print(3*c)
print(a/b)
print(a/c)

## 1.c
# Change a's index values to [2,3,4,5],
a.rename({0:2, 1:3, 2:4, 3:5})
# then display a.
print(a)
#index value does not change

## 1.d
a.rename({0:2, 1:3, 2:4, 3:5}, inplace=True)
# then display a.
print(a)
#index value changes!

## 1.e
print(a+b)
print(b-a)
print(3*c)
print(a/b)
print(a/c)
#for anyting involves a, the length of the pandas series changes!

# Problem 2
## 2.a
#Display a's index; 
print(a.index)
#set variable i equal to a's index and print it; 
i = a.index
print(i)

# display b's first two values; 
print(b[0:2])

# display c's last two values.
print(c[-2:])

## 2b
#Create d as a copy of b but with a's index and display it.
d = b.copy()
d.index = a.index
print(d)

## 2c. Try these: pd.isnull(d) and pd.notnull(d)
print(pd.isnull(d))
print(pd.notnull(d))

## 2d. Assign e as the nonnull entries of d; display it.
e = d[pd.notnull(d)]
print(e)

# Problem 3
## 3a. Create pandas Series named week1 with data [50.0, 25.75, 10.0, 32.5, 15.8] and week2 with data [70.0, 5.8, 2.2, 17.1, 31.1], but make the index of each 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'. Display week1 and week2.
week1 = pd.Series([50.0, 25.75, 10.0, 32.5, 15.8], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
week2 = pd.Series([70.0, 5.8, 2.2, 17.1, 31.1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

## 3b. Assign totals as the sum of week1 and week2. Display it.
totals = week1 + week2
print(totals)

## 3c. Assign diffs as the gain or loss from week1 to week2. Display it.
diffs = week2 - week1
print(diffs)

## 3d. Display week1's values for Monday and Tuesday. Display week2's data for Wednesday through Friday using iloc( ).
print(week1['Monday':'Tuesday'])
print(week2.iloc[2:])   

# Problem 4
## 4a Create the pandas Series named states from the file 'states.csv'. Print it.
df = pd.read_csv('states.csv')
states = pd.Series(df['POPULATION'].values, index=df['NAME'])
print(states)

## 4b Print the index of states
print(states.index)

## 4c. Print the 15th entry of the index. 
# Print the 15th entry of the data using iloc. 
print(states.iloc[14])
# Print that entry again using loc and the name of the state.
name  = states.index.values[14]
print(states.loc[name])



# Lab 5
# Problem 1
## 1a
# create pandas datafram from dictionary of columns
a = pd.DataFrame({'Age':[7, 3,17], 'Breed':['Mix','Corgi', 'Collie']})

# create pandas datafram from list of rows
b = pd.DataFrame([[7, 'Mix'], [3, 'Corgi'], [17, 'Collie']], columns=['Age', 'Breed'])

# make a copy of b; set the index names as listed in the table
c = b.copy()
c.index = ['Fido', 'Barfy', 'Lassie']

print(a)
print(b)
print(c)

## 1b. Display the following: 
# a's zeroth column; 
print(a.iloc[:,0])

# b's first row; 
print(b.iloc[1,:])

# c's 'Lassie' row (by name)
print(c.loc['Lassie'])


## 1c
#Display a's first row, zeroth column; 
print(a.iloc[1,0])
# b's zeroth row, first column; 
print(b.iloc[0,1])
# c's second row, zeroth column.
print(c.iloc[2,0])

## 1d 
# Rename a's index to the names in the table. Display a.
a.rename(index={0:'Fido', 1:'Barfy', 2:'Lassie'}, inplace=True)
print(a)

## 1e
#Add a row to b: 5, Pit Bull (with ignore_index=True). Display b
b = b.append({'Age':5, 'Breed':'Pit Bull'}, ignore_index=True)
print(b)

## 1f
# Add a 'Weight' column to c, setting values at 20, 15, and 35. Display c
c['Weight'] = [20, 15, 35]
print(c)

# Problem 2
#  2a. Create a pandas DataFrame named salesData for the following data. Note: the day names are index values, not a column of data. On Monday, Sales were 2000.43 and Profit was 234.12. On Tuesday, the values were 1887.58 and 184.45; Wednesday, 2729.10 and 302.14; Thursday, 2555.55 and 289.75; Friday, 4208.15 and 441.12. Display salesData
salesData = pd.DataFrame({'Sales':[2000.43, 1887.58, 2729.10, 2555.55, 4208.15], 'Profit':[234.12, 184.45, 302.14, 289.75, 441.12]}, index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
print(salesData)

# 2b Display just the Sales data. Display just the Profit data. Display just Wednesday's data. Display just Thursday's profit.
print(salesData['Sales'])
print(salesData['Profit'])
print(salesData.loc['Wednesday'])
print(salesData.loc['Thursday', 'Profit'])

## 2c Add a new column named '#Customers' with values 12, 10, 8, 11, 22, and display it.
salesData['#Customers'] = [12, 10, 8, 11, 22]
print(salesData)

## 2d Add a new row named 'Saturday' with values 1793.00, 184.57, 9, and display it.
salesData.loc['Saturday'] = [1793.00, 184.57, 9]
print(salesData)

## 2e Print the Sales and Profit totals. 
# For the next three, use Python print formatting for each, with labels: Print just the Sales total. Print just the Profit total. Print just the #Customers total.
#print('Name: {}, Age: {}, Height: {:.2f} meters'.format(name, age, height))

#use formating to print the total sales, profit, and #customers, with 2 digit decimal, and align them to the right
print('Sales total: {:>35.2f}'.format(salesData['Sales'].sum()))
print('Profit total: {:>34.2f}'.format(salesData['Profit'].sum()))
print('#Customers total: {:>30.2f}'.format(salesData['#Customers'].sum()))

## 2f Print the average Sales and average Profit. Print just the name of the day with the largest Sales (this is returned by idxmax() ); do the same for the largest Profit day. Print all the data for the days with the largest Sales; same for the largest Profit.
print('Average Sales: {:>35.2f}'.format(salesData['Sales'].mean()))
print('Average Profit: {:>34.2f}'.format(salesData['Profit'].mean()))
print('Day with largest Sales: {:>26}'.format(salesData['Sales'].idxmax()))
print('Day with largest Profit: {:>25}'.format(salesData['Profit'].idxmax()))
print(salesData.loc[salesData['Sales'].idxmax()])
print(salesData.loc[salesData['Profit'].idxmax()])
