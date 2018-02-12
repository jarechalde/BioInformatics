#In this script we will implement the tournament method to find the maximum and minimum of a number list

arr = [1,3,4,76,43,2,4,7,8]

maxmin = [None,None]
maxminl = [None,None]
maxminr = [None,None]

def findmaxmin(arr,arr0,arr1):

 #If the array has only one element, its the maximum and minimum at the same time
 if arr0 == arr1:
  maxmin[1] = arr[arr0]
  maxmin[0] = arr[arr0]
  return maxmin[1],maxmin[0]
 
 #If the array has two elements
 if arr1 == (arr0 + 1):
  if arr[arr0]>arr[arr1]:
   maxmin[1]= arr[arr0]
   maxmin[0] = arr[arr1]

  else:
   maxmin[1] = arr[arr1]
   maxmin[0] = arr[arr0]
  return maxmin[1],maxmin[0]

 #If there are more than two elements, we should keep dividing the array recursively

 #Now we divide the list in two
 arrmid = (arr0+arr1)/2
 
 maxminl[1],maxminl[0] = findmaxmin(arr,arr0,arrmid)
 maxminr[1],maxminr[0] = findmaxmin(arr,arrmid+1,arr1)
 #Now we compare both maximum and minimum found
 print(maxminl,maxminr)
 
 #Minimum
 if maxminl[0]<maxminr[0]:
  maxmin[0] = maxminl[0]
 else:
  maxmin[0] = maxminr[0]
  
 #Maximum
 if maxminl[1]>maxminr[1]:
  maxmin[1] = maxminl[1]
 else:
  maxmin[1] = maxminr[1]

 print('Relative max: %i Relative min: %i' %(maxmin[1],maxmin[0]))

 return maxmin[1],maxmin[0]

#Calling the function
maxmin = findmaxmin(arr, 0, len(arr)-1)
print('Maximum found: %i' %maxmin[1])
print('Minimum found: %i' %maxmin[0])
