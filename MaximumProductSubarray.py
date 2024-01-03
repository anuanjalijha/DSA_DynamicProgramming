from os import *
from sys import *
from collections import *
from math import *

def maximumProduct(arr, n):
    ans = -100000000000
    
    productFromFront = 1
    productFromBack = 1

    for i in range(0, n):
        
        productFromFront = productFromFront * arr[i]
        productFromBack = productFromBack * arr[n-i-1]

        # Store the maximum of ans, productFromFront and productFromBack in the ans variable.
        ans = max(ans, productFromFront, productFromBack)

        # If any of the products become 0, make them 1 again.
        if productFromFront == 0:
            productFromFront = 1
        if productFromBack == 0:
            productFromBack = 1


    return ans


    # write your code here
    # Return an integer denoting the answer to the required problem 
    