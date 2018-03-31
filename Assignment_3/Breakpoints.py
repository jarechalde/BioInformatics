#Loading the data
data = open('data.txt','r')
data = data.readlines()
data = str.split(data[0], ' ')

mylist = []

#Converting our data from string to integers
for number in data:
 mylist.append(int(number))

#We add 0 to the beggining of the list, and the maximum
#number+1 to the end of it
mylist.insert(0,0)
mylist.append(max(map(abs,mylist))+1)

#Countng the number o breakpoints
def countbreakpoints(list):

 #Initialize the number of breakpoints to 0
 breakpoints = 0

 for i in range(0,len(list)-1):
  number = list[i]
  next_number = list[i+1]

  #If the number is negative it is a decreasing string
  #so the next number it has to be that number+1, if the
  #number is positive is an increasing strin so the next
  #number it also has to be that number+1, else there 
  #is a breakpoint
  if next_number == number+1:
   continue
  else:
   breakpoints = breakpoints+1

 return breakpoints

#Testing our functions
breakpoints = countbreakpoints(mylist)
print('Number of breakpoints: %i' %(breakpoints))
