import math

def isPrime(x):
    prime = True
    if x % 2 == 0:
        prime = False
    else:
        for i in range(2, int(math.sqrt(x) +1)):
            if x % i == 0:
                prime = False
        
    return prime

def highestPrimeFactor(y):
    for i in range(int(math.sqrt(y)+1), 2, -1):
        if y % i == 0 and isPrime(i):
            return i
            


print highestPrimeFactor(600851475143)



