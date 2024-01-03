from os import *
from sys import *
from collections import *
from math import *
def f(i, j, arr):
	if i==j:
		return 0
	if dp[i][j]!=-1:
		return dp[i][j]
	ans = f(i,i,arr)+f(i+1,j,arr)+arr[i]*arr[i+1]*arr[j+1]
	for k in range(i+1,j):
		ans = min(ans,f(i,k,arr)+f(k+1,j,arr)+arr[i]*arr[k+1]*arr[j+1])
	dp[i][j]=ans
	return ans				


def matrixMultiplication(arr, n):
	global dp
	dp = [[-1 for j in range(n)]for i in range(n)]
	return f(0,n-2,arr)
	# Write your code here.

	