# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:38:17 2014

@author: dcelik
"""
def filter_out_negative_numbers(nums):
    newl = []
    for i in nums:
        if i>=0:
            newl.append(i)
    return newl
    
print filter_out_negative_numbers([-2,5,10,-100,5])
print filter_out_negative_numbers([-1,1,2,-2,-100,50,70,20,-1,-8,-9])

def filter_out_negative_numbers_SHORT(nums):
    return [i for i in nums if i>=0]

print filter_out_negative_numbers_SHORT([-2,5,10,-100,5])
print filter_out_negative_numbers_SHORT([-1,1,2,-2,-100,50,70,20,-1,-8,-9])

print range(0,1)

def sum_of_squares(n):
    if n==0:
        return 0
    return (n**2) + sum_of_squares(n-1) 
    
nlist = [i for i in range(0,30)]    
y = [sum_of_squares(i) for i in nlist]
print y