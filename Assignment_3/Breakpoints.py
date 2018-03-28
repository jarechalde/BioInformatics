nlist = [3,4,5,12,-8,-7,-6,1,2,10,9,-11,+13,+14]

newlist = list.append(max(nlist)+1)

def countbreakpoints(list):
 #Initialize the number of breakpoints to 0
 breakpoints = 0

 #Increasing or decreasing strip indicator
 increasing = 0
 decreasing = 0

 for i in range(0,len(list)-1):
  number = list[i]
  next_number = list[i+1]

  #If we haven't found if the strip is decreasing
  #Or increasing we check that
  if increasing == 0 and decreasing == 0:
   if next_number==number+1:
    increasing = 1
    continue
 
   elif next_number==number-1:
    decreasing = 1
    continue

   else:
    breakpoints = breakpoints+1

  if increasing == 1:
   if next_number == number+1:
    continue
   else:
    breakpoints = breakpoints+1
    increasing = 0
    decreasing = 0 
 
  elif decreasing == 1:
   if next_number == number-1:
    continue
   else:
    breakpoints = breakpoints+1
    increasing = 0
    decreasing = 0

 return breakpoints

#We cam also get the number of breakpoints by substracting the number
# of adjacencies to the number of pairs
def countadjacencies(list):
 #Number of pairs
 pairs = len(list) - 1

 #Number of adjacencies
 adjacencies = 0

 for i in range(0,len(list)-1):
  number = list[i]
  next_number = list[i+1]
  
  if next_number == number+1 or next_number == number-1:
   adjacencies = adjacencies + 1
 
 breakpoints = pairs - adjacencies
 
 return breakpoints

#Testing our functions
breakpoints = countadjacencies(nlist)
print('Number of breakpoints: %i' %(breakpoints))
