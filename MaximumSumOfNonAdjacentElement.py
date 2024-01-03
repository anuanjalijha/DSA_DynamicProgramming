from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):
    n = len(nums)
    
    if n == 0:
        return 0
    
    # Array to store previous results.
    dp = [0] * (n + 1)
    
    # Base Cases.
    dp[0] = 0
    dp[1] = nums[0]
    
    for i in range(2,n+1):
        optionA = dp[i - 2] + nums[i - 1]
        optionB = dp[i - 1]
        dp[i] = max(optionA, optionB)
        
    return dp[n]
    
    

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1