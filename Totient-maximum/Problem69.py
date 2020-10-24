# Euler's Totient Function
def phi(n):   

    # Initialize result as n
    result = n
 
    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2
    while(p * p <= n):
         
        # Check if p is a 
        # prime factor.
        if (n % p == 0): 
             
            # If yes, then 
            # update n and result
            while (n % p == 0):
                n = int(n / p)
            result -= int(result / p)
        p += 1
 
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most 
    # one such prime factor)
    if (n > 1):
        result -= int(result / n)
    return result
 
max = 0
nValue = 0
for n in range(2, 1000000, 2):
    if float(n)/phi(n) > max:
        max = float(n)/phi(n)
        nValue = n
        print nValue, phi(n), max
        

resultStatement =  "phi({}) = {}\t {}/phi({}) = {}"
print(resultStatement.format(nValue, phi(nValue), nValue, nValue, max))


    