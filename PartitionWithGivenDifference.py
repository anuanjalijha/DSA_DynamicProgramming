from os import *
from sys import *
from collections import *
from math import *

from typing import List
def f(n,k,arr):
    global dp
    if n==0:
        if k==0:
            return 1
        return 0
    mod = 1000000007
    if dp[n][k]!=-1:
        return dp[n][k]
    if arr[n-1]<=k:
        dp[n][k]=(f(n-1,k-arr[n-1],arr)+f(n-1,k,arr))%mod
    else:
        dp[n][k]=f(n-1,k,arr)%mod 
    return dp[n][k]               

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    global dp
    target_sum = d
    for ele in arr:
        target_sum+=ele
    if target_sum%2!=0:
        return 0
    target_sum = int(target_sum/2)
    dp =[[-1 for j in range(target_sum+1)]for i in range(n+1)]
    return f(n,target_sum,arr)        
    # write your code here

