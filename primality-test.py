# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:33:10 2022

@author: User
"""
import random
def expo(a,n,m):
    if n==0:
        return 1%m
    if n==1:
        return a % m
    ret= expo(a,n//2,m)
    ret= (ret *ret) %m
    if n%2==1:
        ret=(ret*a) %m
    return ret

print(expo(2,5,100000))


def fermat_test(n, k):
    # Implementation uses the Fermat Primality Test
    
    # If number is even, it's a composite number
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, n-1)

        if expo(a, n-1,n) != 1:
            return False
    return True
f=fermat_test(97,20)
print(f)



