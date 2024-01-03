from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
dp =[]
def f(n,w,W,V):
    global dp
    if n==0 or w==0:
        return 0
    if dp[n][w]!=-1:
        return dp[n][w]
    if W[n-1]<=w:
        dp[n][w]=max(f(n-1,w-W[n-1],W,V)+V[n-1],f(n-1,w,W,V))
    else:
        dp[n][w]=f(n-1,w,W,V)
    return dp[n][w]

t = int(input()) 
# global dp
for query in range(t):
    n = int(input())
    weights=list(map(int,input().strip().split(" ")))
    values = list(map(int,input().strip().split(" ")))
    w = int(input()) 
    dp = [[-1 for j in range(w+1)]for i in range(n+1)]
    print(f(n,w,weights,values))                

