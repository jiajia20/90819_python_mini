# Problem 3
import pandas as pd

#a. Create pop1 by using panda's read_csv( ) function, with 'pop1.csv' as the *only* parameter. Print pop1; 
#print the type of pop1; print pop1.describe().
pop1 = pd.read_csv('pop1.csv')
print(pop1)
print(type(pop1))
print(pop1.describe())


#b. The data in pop1.csv can be treated differently than it was in part a by forcing it to be a Series. (Ask yourself: what was it in part a, and why?) Use read_csv( ) with the parameters index_col='State' and squeeze = True. 
# Print pop1; print the type of pop1; print pop1.describe().
pop1 = pd.read_csv('pop1.csv', index_col='State', squeeze = True)
print(pop1)
print(type(pop1))
print(pop1.describe())

#c. Repeat part b for pop2.
pop2 = pd.read_csv('pop2.csv', index_col='State', squeeze = True)
print(pop2)
print(type(pop2))
print(pop2.describe())

#d. Create diff by subtracting pop2 from pop1. Print diff. 
# Print the NaN rows of diff. 
# Print the rows of diff that are negative – use the syntax: myseries[ myseries < 0] – that is, states that lost population.
diff = pop1 - pop2
print(diff)
print(diff[diff.isnull()])
print(diff[diff < 0])

#e. Using that syntax again, print the states whose population is over 1,000,000; 
# print the states whose difference is more than 500,000. 
# Create pct as the diff divided by pop2. Print pct; print the states where that percentage is greater than 0.1.
print(diff[diff > 1000000])
print(diff[diff > 500000])
pct   = diff / pop2
print(pct)
print(pct[pct > 0.1])