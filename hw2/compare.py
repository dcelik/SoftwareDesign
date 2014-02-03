# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 03:57:59 2014

@author: dcelik
"""

def compare(x,y):
    if x>y:
        return 1
    if x==y:
        return 0
    return -1
print "Compare returned "+str(compare(raw_input("Give me an X!\n"),raw_input("Give me a Y!\n")))