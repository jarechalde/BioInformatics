#Number we want to get change for
change = 16784

#Coins we have available to give the change back
coins = [1,3,5,13,15,17,19]


def mincoins(change,coins):
 bestcoins = [0]*(change+1) #Initializing the array that stores the number of coins
 for m in range(1,change+1):
  bestcoins[m] = float('inf') #Initially the best number of coins will be infinite
  for j in range(0,len(coins)):
   coin = coins[j] #Get the coin value for each iteration
   if m>=coin:
    if bestcoins[m-coin]+1<bestcoins[m]:
     bestcoins[m] = bestcoins[m-coin]+1
 
 #Returning the best number of coins
 return bestcoins[change]

#Calling the function and printing the results
bestcoins = mincoins(change,coins)
print('Smallest number of coins: %i' %(bestcoins))
