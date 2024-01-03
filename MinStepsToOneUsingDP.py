from sys import stdin
from sys import maxsize as MAX_VALUE



def countMinStepsToOne(n) :
    if n==1:
        return 0
    minStep = [0]*(n+1) 
    minStep[1]=0
    for currStep in range(2,(n+1)):
        subtractByOne = minStep[currStep-1]
        divisibleByTwo =  MAX_VALUE
        divisibleByThree =  MAX_VALUE
        if currStep%2==0:
            divisibleByTwo = minStep[currStep//2]
        if currStep%3==0:
            divisibleByThree = minStep[currStep//3]
        minStep[currStep]=1+min(subtractByOne,divisibleByTwo,divisibleByThree) 
    return minStep[n]       
            


    



#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))