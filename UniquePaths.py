def isValid(n,m,mat):
    N= len(mat)
    M = len(mat[0])
    if n<0 or n>=N or m<0 or m>=M or mat[n][m]==-1:
        return False
    return True    
def f(n,m,N,M,mat,dp):
    mod =1000000007
 
    # global dp
    if n==N-1 and m==M-1:
        return 1
    if dp[n][m]!=-1:
        return dp[n][m]
    ans = 0    
    if isValid(n,m+1,mat):
        ans+=f(n,m+1,N,M,mat,dp)
    if isValid(n+1,m,mat):
        ans+=f(n+1,m,N,M,mat,dp)
    ans%=mod   
    dp[n][m]=ans
    return ans    
                
def mazeObstacles(n, m, mat):
    # global dp 
    dp = [[-1 for j in range(m)]for i in range(n)]
    return f(0,0,n,m,mat,dp)
    # Write your code here.
