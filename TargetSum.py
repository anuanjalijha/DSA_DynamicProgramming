from os import *
from sys import *
from collections import *
from math import *

from typing import List
def getNumOfWays(arr: List[int], target: int, index: int,memo: dict) -> int:

    # Base Case.
    if index > len(arr) - 1:
        return 1 if target == 0 else 0
    if (index, target) in memo:
        return memo[(index, target)]

    

    # Take the sum of both possibilities.
    ans = getNumOfWays(arr, target - arr[index], index + 1,memo)
    ans += getNumOfWays(arr, target + arr[index], index + 1,memo)
    memo[(index, target)] = ans

    # Return the sum.
    return ans


def targetSum(arr: List[int], target: int) -> int:
    memo = {}
    return getNumOfWays(arr, target, 0,memo)
    pass
