# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:09:50 2022

@author: User
"""
'''
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
'''
def equation_solver(a,b,m):
    for x in range(m):     # O (M)
        if a *x %m == b:
            return print(" From eq solver:",x)
    return -1
equation_solver(13, 7, 11)

#extended euclidean algorithm
def gcd(a,b):
    if b==0:
        return a,1,0
    g,_x, _y=gcd(b,a%b)
    
    x=_y
    y= _x - (a//b)* _y
    
    return g,x,y

a, n=13, 11
gcd, _x, _y=gcd(a,n)

b=7

if b//gcd:
    x= _x * (b//gcd)
    x=x%n
    if x<0:
        x+=n
    print("From extended euclid:",x)
else:
    print("No solution")

