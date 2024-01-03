from os import *
from sys import *
from collections import *
from math import *

from typing import *
def f(n,N,heights):
    global dp
    if n==N:
        return 0
    elif n==N-1:
        return abs(heights[N-1]-heights[N-2])
    
    if dp[n]!=-1:
        return dp[n] 
    else:
        dp[n]= min(f(n+1,N,heights)+abs(heights[n-1]-heights[n]),f(n+2,N,heights)+abs(heights[n-1]-heights[n+1]))           
        return dp[n]

  
def frogJump(n: int, heights: List[int]) -> int:
    global dp 
    dp = [-1]*(n+1)
    return f(1,n,heights)

    # Write your code here.
    pass
