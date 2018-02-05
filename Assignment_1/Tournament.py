#In this script we will implement the tournament method to find the maximum and minimum of a number list

arr = [1,3,4,76,43,2,4,7,8]

maxmin = {'Max': None, 'Min': None}
maxminT = {'Max': None, 'Min': None}


maxminL1 = {'Max': None, 'Min': None}
maxminL2 = {'Max': None, 'Min': None}

maxminl = {'Max': None, 'Min': None}



def findmaxmin(arr,arr0,arr1,maxminL1,maxminL2):
 
 print('DOWN')
 print(arr0,arr1)

 try:
  print('Hola>')
  #print(maxminL1,maxminL2)
  print('Hola>')
 except:
  pass

 #If the array has only one element, its the maximum and minimum at the same time
 if arr0 == arr1:
  print('Length == 1')
  maxmin['Max'] = arr[arr0]
  maxmin['Min'] = arr[arr0]
  print('Array length 1: ', maxmin)
  print('UP')
  return maxmin
 
 #If the array has two elements
 if arr1 == (arr0 + 1):
  print('Length == 2')
  
  if arr[arr0]>arr[arr1]:
   print('We here')
   maxmin['Max']= arr[arr0]
   maxmin['Min'] = arr[arr1]

  else:
   print('Or here')
   maxmin['Max'] = arr[arr1]
   maxmin['Min'] = arr[arr0]
   
  print('Array length 2: ', maxmin)
  print('UP')
  return maxmin

 #If there are more than two elements, we should keep dividing the array recursively

 #Now we divide the list in two
 print('Dividing Array')
 arrmid = (arr0+arr1)/2
 arr0 = int(arr0)
 arr1 = int(arr1)

 print('Arr0: %i Arr1: %i' %(arr0,arr1))

 print('Left half')
 maxminL1 = findmaxmin(arr,arr0,arrmid,maxminL1,maxminL2)
 print(maxminL1)
 maxminl['Max'] = maxminL1['Max']
 maxminl['Min'] = maxminL1['Min']
 
 print('Saved L1', maxmin)
 print('Right half')
 maxminL2 = findmaxmin(arr,arrmid+1,arr1,maxminL1,maxminL2)

 print('Relative max and min: ')
 print(maxminl)
 print(maxminL2)
 print('\n\n')

 #Now we compare both maximum and minimum found

 #Maximum
 if maxminL1['Max']>maxminL2['Max']:
  maxminT['Max'] = maxminL1['Max']
 else:
  maxminT['Max'] = maxminL2['Max']

 #Minimum
 if maxminL1['Min']<maxminL2['Min']:
  maxminT['Min'] = maxminL1['Min']
 else:
  maxminT['Min'] = maxminL2['Min']

 print('Relative max: %i Relative min: %i' %(maxminT['Max'],maxminT['Min']))

#Calling the function
print('Calling the function')
findmaxmin(arr, 0, len(arr)-1,maxminL1,maxminL2)
print('Maximum found: %i' %maxminT['Max'])
print('Minimum found: %i' %maxminT['Min'])
