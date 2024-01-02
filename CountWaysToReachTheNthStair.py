def countDistinctWays(nStairs: int) -> int:
    dp = [0] * (nStairs + 1)
    if nStairs==0 or nStairs==1:
        return 1
    mod = 1000000007    

    # Base cases: there is one way to reach the 0th and 1st steps
    dp[0] = 1
    dp[1] = 1

    # Iterate from the 2nd step to the nth step
    for i in range(2, nStairs + 1):
        # The number of ways to reach the current step is the sum of
        # the ways to reach the previous two steps
        dp[i] = (dp[i - 1] + dp[i - 2])%mod

    # The result is stored in dp[n], which represents the number of ways to reach the nth step
    return dp[nStairs]

