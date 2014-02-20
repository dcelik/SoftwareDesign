# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:04:21 2014

@author: dcelik
"""

def levenshtein_distance(s1,s2,d={}):
    """ 
    Computes the Levenshtein distance between two input strings 
    """
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    elif (s1,s1) in d:
        return d[(s1,s2)]
    else:
        x = min([int(s1[0] != s2[0]) + levenshtein_distance(s1[1:],s2[1:]), 1+levenshtein_distance(s1[1:],s2), 1+levenshtein_distance(s1,s2[1:])])
        d[(s1,s2)]=x
        return x
print levenshtein_distance("denizecelik","ryanlouie")