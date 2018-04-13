#Import numpy
import numpy as np

#Input strings
#ATCG = 1234
v = ['T','A','C','G','G','G','T','A','T']
w = ['G','G','A','C','G','T','A','C','G']

#One matrix with arrows other with scores
dist_mat = np.zeros((len(v),len(w)))
arr_mat = np.zeros((len(v),len(w)), dtype='|S6')

match = 1
mismatch = -1

for i in range(0,len(v)):
 dist_mat[i,0] = i
 arr_mat[i,0] = 'U' 

for j in range(0,len(w)):
 dist_mat[0,j] = j
 arr_mat[0,j] = 'L'

for i in range(1,len(v)):
 for j in range(1,len(v)):
  values = np.zeros(3)

  values[0] = dist_mat[i-1,j] + 1
  values[1] = dist_mat[i,j-1] + 1
  values[2] = float('inf')

  if v[i] == w[j]:
   values[2] = dist_mat[i-1,j-1] 

  minval  = np.argmin(values) #Position of the first maximum of values

  dist_mat[i,j] = values[minval]

  if minval == 0:
   arr_mat[i,j] = 'U'
  if minval == 1:
   arr_mat[i,j] = 'L'
  if minval == 2:
   arr_mat[i,j] = 'D'

print(dist_mat)
print(arr_mat)

#Now we do the backtracking

i = len(v) - 1
j = len(w) - 1

while (True):
 dir = arr_mat[i,j]

 print(dist_mat[i,j])
 print(arr_mat[i,j])
  
 if dir == 'L': #Then we have to go left
  j = j-1
 
 elif dir == 'D':
  i = i-1
  j = j-1

 elif dir == 'U':
  j = j-1

 else:
  break  
