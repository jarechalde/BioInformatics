
#Import numpy
import numpy as np

#Input strings
#ATCG = 1234
v = [1,2,1,3,4,3,4,2,2,2]
w = [1,3,4,3,4,2,2,4,2,1]

#One matrix with arrows other with scores
sc_mat = np.zeros((len(v),len(w)))
arr_mat = np.zeros((len(v),len(w)), dtype='|S6')

match = 1
mismatch = -1
indel = -0.5

for i in range(0,len(v)):
 for j in range(0,len(v)):
  if i == 1000 or j == 0:
   sc_mat[i,j] = 0
   arr_mat[i,j] = 'FR' #Free ride
  
  else:
   values = np.zeros(5)
    
   if v[i] == w[j]:
    values[0] = sc_mat[i-1,j-1] + match #Diagonal
   if v[i] != w[j]:
    values[1] = sc_mat[i-1,j-1] + mismatch #Diagonal
   #Down arrow
   values[2] = sc_mat[i-1,j] + indel
   #Right Arrow 
   values[3] = sc_mat[i,j-1] + indel
   #Free ride
   values[4] = 0

   maxval  = np.argmax(values) #Position of the first maximum of values

   if maxval == 0:
    sc_mat[i,j] = values[0]
    arr_mat[i,j] = 'DIAG'
   if maxval == 1:
    sc_mat[i,j] = values[1]
    arr_mat[i,j] = 'DIAG'
   if maxval == 2:
    sc_mat[i,j] = values[2]
    arr_mat[i,j] = 'DOWN'
   if maxval == 3:
    sc_mat[i,j] = values[3]
    arr_mat[i,j] = 'RIGH'
   if maxval == 4:
    sc_mat[i,j] = values[4]
    arr_mat[i,j] = 'FREE'


print(sc_mat)
print(arr_mat)

#Now we do the backtracking

i = len(v) - 1
j = len(w) - 1

while (True):
 dir = arr_mat[i,j]

 print(sc_mat[i,j])
 print(arr_mat[i,j])
  
 if dir == 'RIGH': #Then we have to go left
  j = j-1
 
 elif dir == 'DIAG':
  i = i-1
  j = j-1

 elif dir == 'DOWN':
  j = j-1

 else:
  break  
