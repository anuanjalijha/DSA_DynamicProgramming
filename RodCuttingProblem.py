from sys import stdin
import sys

def cutRod(price, n):
    cost = [0 for x in range(n+1)]
    cost[0] = 0

    # Build the table in bottom up manner.
    for i in range(1, n+1):
        maxCost = -sys.maxsize-1

        for j in range(i):
            maxCost = max(maxCost, price[j] + cost[i - j - 1])

        # Contains maximum cost obtained from the rod of length 'i'.
        cost[i] = maxCost

    # Last entry conatins maximum cost obtained from the rod of length 'n'.
    return cost[n]

    # Write your code here.
    

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
