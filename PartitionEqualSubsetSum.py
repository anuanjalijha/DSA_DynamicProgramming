def canPartition(arr, n):
     # It stores the sum of all array element.
    totalsum = 0

    # Iterating the array.
    for num in arr:
        totalsum += num

    # If totalsum is odd, then it can't be partitioned into equal sum subsets.
    if totalsum % 2 != 0:
        return False
    
    # One subset sum will always be totalSum/2.
    subsetsum = totalsum // 2
    
    # Create a new auxiliary array dp.
    dp = [[None for i in range(subsetsum + 1)] for j in range(n+1)]
    
    dp[0][0] = True
    
    for i in range(1,n+1):
        for j in range(subsetsum+1):
            if (arr[i - 1] <= j):
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i-1][j]
            else:

                dp[i][j] =dp[i - 1][j]
            
        
    return dp[n][subsetsum]

    # Write your code here.
    