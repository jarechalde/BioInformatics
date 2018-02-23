#Importing numpy module
import numpy as np
from itertools import permutations

#We are given the following partial digest
L = [1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,9,9,10,11,12,15]

def anotherbruteforcepdp(L):
 M = max(L)
 Ll = len(L)
 
 #Calculating n
 #n^2-n-2*L = 0
 n = (1+np.sqrt(1+8*Ll))/2
 
 if (int(n) != n):
  print('Error')
  return

 n = int(n)

 print('Maximum: %i Length: %i' %(M,n))

 #First we need to get the unique integers
 UL = []
 for number in L:
  if UL == []:
   UL.append(number)
  else:
   if number != UL[len(UL)-1] and number<M and number>0:
   	UL.append(number)
   else:
   	continue

 #List of good sets
 XList = []
 
 #Valid X
 Xret = []

 #Now we will build all the different possible sets, using the itertools package
 for p in permutations(UL, 5):
  valid = 1

  #We check if the set is valid
  for i in range(0,len(p)-1):
  	if p[i]>=p[i+1]:
  	 valid = 0
  #If the set is valid, we create X
  if valid == 1:
  	p = list(p)
  	p.insert(0,0)
  	p.append(M)
  	XList.append(p) #Adding set to the list of sets

 #For each set, we check if deltaX equals L
 for X in XList:
  
  dx =[]

  for i in range(0,len(X)):
   for j in range(i+1,len(X)):
    deltax = X[j]-X[i]
    dx.append(deltax)

  #Sorting the Delta X list
  dx.sort()

  if dx == L:
  	Xret.append(X)

 #If we finish iterating the for loop without finding any solution we
 #return that there is no solution

 if Xret == []:
  print('No solution')
  return

 else:
  return Xret

#We call the function and store the results
X = anotherbruteforcepdp(L)

print('')
print('X Found:')
print(X)