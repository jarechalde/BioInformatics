arr0 = [0,0,0]
arr1 = [2,2,2]
d = len(arr1)-1

darr = [0]*len(arr1)
arr = [0]*len(arr1)

def rec1(arr0,arr1,depth,darr,arr):

 if(depth<d):
  darr = rec1(arr0,arr1,depth+1,darr,arr)

 print(darr[depth],arr1[depth])

 for i in range(darr[depth],arr1[depth]+1):
  arr[depth] = i
  print(arr)


 if arr[depth-1]==arr1[depth-1]:
  d
 arr[depth-1] = arr[depth-1]+1
 
 return(darr)

rec1(arr0,arr1,0,darr,arr)
