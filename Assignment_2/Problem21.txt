#First we declare the X
X =[1,2,4,6,9,14]

#We will store DX in this list
dx =[]

#Now we will iterate over the list to calculate all the distances
for i in range(0,len(X)):
 for j in range(i+1,len(X)):
  deltax = X[j]-X[i]
  dx.append(deltax)

#Print the results
print('X:')
print(X)
print('')
print('Delta X:')
print(dx)