import random

def sum2():
    '''This gives output of 2 random numbers'''
    a = random.random()
    b = random.random()

    return a+b

def sumkrand(k):
    '''gives sum of k random numbers'''
    ans = 0
    for i in range(k):
        ans = ans + random.random()
    
    return ans
