
#Import numpy
import numpy as np

#Input strings
#ATCG = 1234
v = [1,2,1,3,4,3,4,2,2,2]
w = [1,3,4,3,4,2,2,4,2,1]

#One matrix with arrows other with scores
sc_mat = np.zeros((len(v)+1,len(w)+1))
arr_mat = np.zeros((len(v)+1,len(w)+1), dtype='|S6')

match = 1
mismatch = -1
indel = -0.5

for i in range(0,len(v)+1):
 sc_mat[i,0] = 0
 arr_mat[i,0] = 'FR' #Free ride
  
for j in range(0,len(w)+1):
 sc_mat[0,j] = 0
 arr_mat[0,j] = 'FR' #Free ride
  

for i in range(0,len(v)):
 for j in range(0,len(v)):

  values = np.zeros(5)

  #Match
  if v[j] == w[i]:
   values[0] = sc_mat[i,j] + match #Diagonal
  else:
   values[0] = -float('inf')

  #Mismatch
  if v[j] != w[i]:
   values[1] = sc_mat[i,j] + mismatch #Diagonal
  else:
   values[1] = -float('inf')

  #Down arrow
  values[2] = sc_mat[i,j+1] + indel

  #Right Arrow 
  values[3] = sc_mat[i+1,j] + indel

  #Free ride
  values[4] = 0

  maxval  = np.argmax(values) #Position of the first maximum of values

  if maxval == 0:
   sc_mat[i+1,j+1] = values[0]
   arr_mat[i+1,j+1] = 'DI'
  if maxval == 1:
   sc_mat[i+1,j+1] = values[1]
   arr_mat[i+1,j+1] = 'DI'
  if maxval == 2:
   sc_mat[i+1,j+1] = values[2]
   arr_mat[i+1,j+1] = 'DO'
  if maxval == 3:
   sc_mat[i+1,j+1] = values[3]
   arr_mat[i+1,j+1] = 'RI'
  if maxval == 4:
   sc_mat[i+1,j+1] = values[4]
   arr_mat[i+1,j+1] = 'FR'


print(sc_mat)
print('')
print(arr_mat)

a,b = sc_mat.shape #Shape of the score matrix

maxpos = []
maxval = 0
#Find the highest value and backtrack
for i in range(0,a):
 for j in range(0,b):
  val = sc_mat[i,j]
  if val>maxval:
   maxval = val
   maxpos = []
   maxpos.append([i,j])
  elif val == maxval:
   maxpos.append([i,j])
  else:
   continue

#Now we do the backtracking
for position in maxpos:

 i = position[0]
 j = position[1]

 alignv = ''
 alignw = ''

 while (True):

  dir = arr_mat[i,j]

  if dir == 'RI': #INSERTION
   alignv = '-'+alignv 
   alignw = str(w[j-1])+alignw
   j = j-1
 
  elif dir == 'DI':
   alignv = str(v[j-1])+alignv
   alignw = str(w[i-1])+alignw
   i = i-1
   j = j-1

  elif dir == 'DO': #DELETION
   alignv = str(v[i-1])+alignv
   alignw = '-'+alignw
   i = i-1
  
  else:
   break  
 
 print('')
 print('ALIGNMENT:')
 print(alignv)
 print(alignw)
