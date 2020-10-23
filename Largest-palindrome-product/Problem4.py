# coding=utf-8
def isPalindrome(x):
    y = str(x)
    y = y[::-1]
    y = int(y)
    if x == y:
        return True
    else:
        return False

def largestPalindrome():
    high = 999*999
    for i in range(high, 1, -1):
        if isPalindrome(i):
            for y in range(999, 1, -1):
                if i % y == 0 and i / y < 999:
                    factors = "The largest palindrome made from the product of two 3-digit numbers is {} = {} × {}."
                    print(factors.format(i, y, i/y)) 
                    return 1

largestPalindrome()