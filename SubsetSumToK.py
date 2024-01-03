from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
     # Declaring dp array
    dp = [[False for i in range(k + 1)] for i in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    # If size of array = 0, answer always false
    for j in range(1, k + 1):
        dp[0][j] = False
        
    # Filling dp array
    for i in range(1, n + 1):
        
        for j in range(1, k + 1):
            
            dp[i][j] = dp[i - 1][j]
            
            if(arr[i - 1] <= j):
                
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]
                
    return dp[n][k]
        
        
    

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer

    
    
    

