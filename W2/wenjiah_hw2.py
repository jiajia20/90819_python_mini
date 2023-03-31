# Problem 1

#a
# Create numpy arrays a, b, and c by reading the CSV files (a from a.txt, etc.); 
#set their type as dtype = int. 
#Print each one.

import numpy as np
a = np.loadtxt('a.txt', delimiter=',')
print(a)

b = np.loadtxt('b.txt', delimiter=',')
print(b)

c = np.loadtxt('c.txt', delimiter=',')
print(c)

#b. Print the shape of the three arrays, with labels, as in: 'Shape of a is 4x4' (hint: the shape is a tuple).

print('Shape of a is', a.shape)
print('Shape of b is', b.shape)
print('Shape of c is', c.shape)

#c. Print the results of multiplying (using the "real" linear algebra multiplication function, dot( ) ) of a times b, b times c, and b transpose times a.

print(np.dot(a,b))
print(np.dot(b,c))
print(np.dot(b.T,a))

#d. Save a, b, and c to binary files. 
#Read those files back into new arrays anew, bnew, and cnew. 
#Print a == anew and the same for bnew and cnew, as proof that your binary read/write is correct.

np.save('a.npy', a)
np.save('b.npy', b)
np.save('c.npy', c)

anew = np.load('a.npy')
bnew = np.load('b.npy')
cnew = np.load('c.npy')

print(a == anew)


#e. Create array d by reshaping a to be 2 by 8; 
#print it; print its shape with a label. 
#Create array e by reshaping a to be 8 by 2; 
#print it; print its shape with a label.

d = a.reshape(2,8)
print(d)
print('Shape of d is', d.shape)
e = a.reshape(8,2)
print(e)
print('Shape of e is', e.shape)

#problem 2

## Getting input
f = float(input("Enter the fox growth rate: ")) #0.6

c = float(input("Enter the chicken growth rate: ")) #1.2

e= float(input("Enter the eat-chicken rate: ")) #0.5

k = float(input("Enter kill rate: ")) #0.5

iter = int(input("Enter number of iterations: ")) #2

#print the time period, chicken and fox population 

print('{:<20} {:<15} {:<15}'.format('Time period', '# foxes', '# chickens'))

print()

## calculate the result of somulation for i times
fox = 100
chicken = 1000
print('{:<20} {:<15} {:<15}'.format(0, fox, chicken))

for i in range(iter):
    result = np.array([[f, e], [-k, c]]).dot(np.array([fox, chicken]))
    fox = result[0]
    chicken = result[1]
    print('{:<20} {:<15} {:<15}'.format(i, fox, chicken))
