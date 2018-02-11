import numpy as np

def fib(n):
    if n==0:
        return 0
    arr = np.zeros(n+1) #Create the array to store the fib. numbers
    arr[0] = 0
    arr[1] = 1
    
    for i in range(2,n+1):
        arr[i] = arr[i-1]+arr[i-2]

    #Return fib(n)
    return arr[n]

f = fib(23)

print(f)
        
