# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:01:04 2014

@author: dcelik
"""

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
    
print [fib(i) for i in range(1,10)]

fibdict={}
def fibonacci(n,d={}):
    if n==0 or n==1:
        return n
    elif n in d:
        return d[n]
    else:
        x = fibonacci(n-2)+fibonacci(n-1)
        d[n]=x
        return x
print fibonacci(100)