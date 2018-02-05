#In this script we will implement the tournament method to find the maximum and minimum of a number list

arr = [1,3,4,76,43,2,4,7,8]

maxmin = {'Max': None, 'Min': None}

def findmaxmin(arr,arr0,arr1):
 
 print('Recurring')
 print(arr0,arr1)

 #If the array has only one element, its the maximum and minimum at the same time
 if arr0 == arr1:
  print('Length == 1')
  maxmin.Max = arr[arr0]
  maxmin.Min = arr[arr0]
  print('Array length 1: ', maxmin)
  return maxmin
 
 #If the array has two elements
 if arr1 == (arr0 + 1):
  print('Length == 2')
  if arr[arr0]>arr[arr1]:
   maxmin['Max']= arr[arr0]
   maxmin['Min'] = arr[arr1]

  else:
   maxmin['Max'] = arr[arr1]
   maxmin['Min'] = arr[arr0]
  print('Array length 2: ', maxmin)
  return maxmin

 #If there are more than two elements, we should keep dividing the array recursively

 #Now we divide the list in two
 arrmid = (arr0+arr1)/2

 maxminL1 = findmaxmin(arr,arr0,arrmid)
 maxminL2 = findmaxmin(arr,arrmid,arr1)

 print(maxminL1,maxminL2)
 print('\n\n')

 #Now we compare both maximum and minimum found

 #Maximum
 if maxminL1['Max']>maxminL2['Max']:
  maxmin['Max'] = maxminL1['Max']
 else:
  maxmin['Max'] = maxminL2['Max']

 #Minimum
 if maxminL1['Min']<maxminL2['Min']:
  maxmin['Min'] = maxminL1['Min']
 else:
  maxmin['Min'] = maxminL2['Min']

findmaxmin(arr, 0, len(arr)-1)
print('Maximum found: %i' %maxmin['Max'])
print('Minimum found: %i' %maxmin['Min'])
