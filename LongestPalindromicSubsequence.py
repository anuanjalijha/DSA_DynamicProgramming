from os import *
from sys import *
from collections import *
from math import *
def longestPalindromeSubsequenceHelper(s, i, j):
    global dp
    # Base Case 1: If there is only 1 character.
    if (i == j):
        return 1
        
    
    # Base Case 2: If there are only 2 characters and both are same.
    if(s[i] == s[j] and i + 1 == j):
        return 2
    if dp[i][j]!=-1:
        return dp[i][j]    
    
    # If the first and last characters match.
    if(s[i] == s[j]):

        dp[i][j]= longestPalindromeSubsequenceHelper(s, i + 1, j - 1) + 2
    else:    
    
    # If the first and last characters do not match.
        op1 = longestPalindromeSubsequenceHelper(s, i, j - 1)
        op2 = longestPalindromeSubsequenceHelper(s, i + 1, j)
    
        dp[i][j]= max(op1, op2)
    return dp[i][j] 
def longestPalindromeSubsequence(s):
    global dp
    n = len(s)
    dp = [[-1] * n for _ in range(n)]

    return longestPalindromeSubsequenceHelper(s, 0, len(s) - 1)
    # Write your code here.

