from os import *
from sys import *
from collections import *
from math import *
def houseRobberUtil(valueInHouse, start, end):
    
    
    valueAtIthHouse = [-1 for i in range(len(valueInHouse))]

    # Check if thief may steal first huse or not.
    if (start == 0):
        valueAtIthHouse[0] = valueInHouse[0]
        valueAtIthHouse[1] = max(valueInHouse[0], valueInHouse[1])

    else:
        valueAtIthHouse[0] = 0
        valueAtIthHouse[1] = valueInHouse[1]

    for i in range(2, end):
        valueAtIthHouse[i] = max(valueAtIthHouse[i - 2] + valueInHouse[i], valueAtIthHouse[i - 1])

    return valueAtIthHouse[end - 1]


def houseRobber(valueInHouse):
    if (len(valueInHouse) == 0):
        return 0

    if len(valueInHouse) == 1:
        return valueInHouse[0]

    return max(houseRobberUtil(valueInHouse, 0, len(valueInHouse) - 1), houseRobberUtil(valueInHouse, 1, len(valueInHouse)))

    # Write your function here.
    