
from sys import stdin
def f(n,m,s,t):
	global dp
	if n==0 or m==0:
		return 0
	if dp[n][m]!=-1:
		return dp[n][m]
	if s[n-1]==t[m-1]:
		dp[n][m]=f(n-1,m-1,s,t)+1
	else:
		dp[n][m]=max(f(n-1,m,s,t),f(n,m-1,s,t))	
	return dp[n][m]				

def lcs(s, t) :
	global dp
	n = len(s)
	m = len(t)
	dp =[[-1 for j in range(m+1)]for i in range(n+1)]
	return f(n,m,s,t)
	#Your code goes here






























    


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))