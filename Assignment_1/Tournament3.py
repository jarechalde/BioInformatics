#In this script we will implement the tournament method to find the maximum and minimum of a number list

arr = [1,3,4,76,43,2,4,7,8]

maxminT = {'Max': None, 'Min': None}

maxminl = {'Max': None, 'Min': None}
maxminr = {'Max': None, 'Min': None}

def findmaxmin(arr,arr0,arr1):

 print(maxminl,maxminr)

 #If the array has only one element, its the maximum and minimum at the same time
 if arr0 == arr1:
  amax = arr[arr0]
  amin = arr[arr0]
  print(amax,amin)
  return amax,amin
 
 #If the array has two elements
 if arr1 == (arr0 + 1):
  if arr[arr0]>arr[arr1]:
   amax = arr[arr0]
   amin = arr[arr1]

  else:
   amax = arr[arr1]
   amin = arr[arr0]
  print(amax,amin)
  return amax,amin

 #If there are more than two elements, we should keep dividing the array recursively

 #Now we divide the list in two
 arrmid = (arr0+arr1)/2
 
 maxminl['Max'],maxminl['Min'] = findmaxmin(arr,arr0,arrmid)
 maxminr['Max'],maxminr['Min']  = findmaxmin(arr,arrmid,arr1)

 #Now we compare both maximum and minimum found
 print('WTF')
 print(maxminl['Max'],maxminr['Max'])


 #Maximum
 if maxminl['Max']>maxminr['Max']:
  maxminT['Max'] = maxminl['Max']
 else:
  maxminT['Max'] = maxminr['Max']

 print(maxminT)

 #Minimum
 if maxminl['Min']<maxminr['Min']:
  maxminT['Min'] = maxminl['Min']
 else:
  maxminT['Min'] = maxminr['Min']

 print(maxminT)
 #print('Relative max: %i Relative min: %i' %(maxminT['Max'],maxminT['Min']))

 return maxminT
 
#Calling the function
maxminT = findmaxmin(arr, 0, len(arr)-1)
print('Maximum found: %i' %maxminT['Max'])
print('Minimum found: %i' %maxminT['Min'])
