#Name: Wenjia Hu

#Lab 2
# Problem 1
#Create a list variable named numbers and set it to the integers -5 to 5 inclusive
numbers = list(range(-5,6))

#Save the contents of numbers to a text file named 'numbers.txt', one int per line
with open('numbers.txt', 'w') as f:
    for i in numbers:
        f.write('%d\n' % (i))   


# Problem 2
myNums = []
#Open 'numbers.txt' for reading and read the line and convert it to int, one at a time, into myNums. 
with open('numbers.txt', 'r') as f:
    for line in f:
        myNums.append(int(line))

# Display the list.
print (myNums)
# Then use print(numbers == myNums) to verify that it has the same int as numbers in #1.
print(numbers == myNums)



# Problem 3
data = [('Fido', 12), ('Barfy', 8), ('Spot', 5), ('Yeller', 15)]
import pickle

print(data)

with open('mydata.bin', 'wb') as f:
    pickle.dump(data, f)

# Problem 4
# Open the file 'mydata.bin' with 'rb' access. 
# Use pickle to read its contents into a variable named newdata.
with open ('mydata.bin', 'rb') as f:
    newdata = pickle.load(f)
 
#Display the type of newdata to verify that it is a list. 
print(type(newdata))
# Then display newdata and use print(data == newdata) to verify that the data is the same in #5
print(newdata == data)

# Problem 5
# (a.) Create numpy arrays named x, y, N, and I as:
# x: the floats from 1 to 3 counting by 0.5; use arange( ), but reshape it to (4,1) 
# y: from the list [-1.0, 1.0, -1.0, 1.0], but reshape it to (4,1)
# N: from the list of lists [ [0, 1, 1, 0], [3, 2, 1, 0] ]
# I: the 4x4 identity matrix

x = np.arange(1,3,0.5).reshape(4,1)
y = np.array([-1.0, 1.0, -1.0, 1.0]).reshape(4,1)
N = np.array([[0, 1, 1, 0], [3, 2, 1, 0]])
I = np.identity(4)



# (b.) Display each array.
print(x)
print(y)
print(N)
print(I)

# (c.) Display each array's shape (size)
print(x.shape)
print(y.shape)
print(N.shape)
print(I.shape)

# (d.) Display each array's dimensionality (ndim) 
print(x.ndim)
print(y.ndim)
print(N.ndim)
print(I.ndim)

# (e.) Display N's zeroth row using a slice
print(N[0]) 

# (f.) Display N's zeroth column using a slice
print(N[:,0])

# Problem 6
#  For each problem, tell which operations are legal - *before* entering them. Then execute and print them. 
# (a.) x+y
print(x+y)


# (b.) x*y
print(x*y)
# (c.) x.dot(y) ## Not LEGAL, dimention does not match
# print(x.dot(y))

# (d.) (x.T).dot(y) 
print((x.T).dot(y))

#(e.) x.dot(y.T) 
print(x.dot(y.T))

# (f.) N*N
print(N*N)
# (g.) x*N
# print(x*N) NOT LEGAL, dimention does not match

# (h.) x.dot(N) 
# print(x.dot(N)) not legal, dimention does not match

# (i.) (x.T).dot(N) 
#print((x.T).dot(N)) not legal, dimention does not match
# (j.) N.dot(x)
print(N.dot(x))