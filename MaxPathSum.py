from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
def isValid(n,m,matrix):
    N=len(matrix)
    M = len(matrix[0])
    if n<0 or n>=N or m<0 or m>=M:
        return False
    
    return True
def f(n,m,N,M,matrix):
    global dp
    if n==N-1:
        return matrix[n][m]
    if dp[n][m]!=float('-inf'):
        return dp[n][m]
    ans = f(n+1,m,N,M,matrix)
    if isValid(n+1,m-1,matrix):
        ans = max(ans,f(n+1,m-1,N,M,matrix))
    if isValid(n+1,m+1,matrix):
        ans = max(ans,f(n+1,m+1,N,M,matrix))
    ans+=matrix[n][m]
    
    dp[n][m]=ans
    return ans    
                            


def getMaxPathSum(matrix):
    m =len(matrix[0])
    n = len(matrix)
    global dp 
    dp= [[float('-inf')for j in range(m)]for i in range(n)]
    ans = float('-inf')
    for i in range(m):
        ans = max(ans,f(0,i,n,m,matrix))
    return ans    

    #   Write your code here
    pass


























#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
