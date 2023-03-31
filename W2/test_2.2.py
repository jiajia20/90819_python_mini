import numpy as np
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