from typing import List

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)

    # Initialize a 2d matrix 'DP' of size ('N'+1) x ('k'+1) with value 0.
    dp = [[0 for _ in range(k + 1)] for _ in range(n+1)]

    # Set 'DP[0][0]' = 1.
    dp[0][0] = 1

    # Run a loop from 'j' = 1...'k':
    for j in range(1, k + 1):
        # Set 'DP[ 0 ][ j ]' = 0
        dp[0][j] = 0

    # Run a loop from 'i' = 1...'N':
    for i in range(1, n + 1):
        # Run a loop from 'j' = 0...'k':
        for j in range(k + 1):
            # If the value of 'NUM' at 'i'-1 <= 'j' then set
            # 'DP[ i ][ j ]' = 'DP[ i-1 ][ j ]' + 'DP[ i-1 ][ j - num[ i-1 ] ]'.
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
            else:
                # Else Set 'DP[ i ][ j ]' = 'DP[ i-1 ][ j ]'.
                dp[i][j] = dp[i - 1][j]
    # Return the value of 'DP[ N ][ k ]'.
    return dp[n][k] % (10**9 + 7)

    # Write your code here.
