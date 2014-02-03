# -*- co<ding: utf-8 -*-
"""
Created on Mon Feb  3 03:23:32 2014

@author: dcelik
"""

def fermat(a,b,c,n):
    part1 = a**n + b**n
    part2 = c**n
    if n<=2:
        print "n must be greater than 2!"
    elif a**n + b**n == c**n:
        print "Holy Smokes, Fermat was Wrong"
    else:
        print "No, that doesn't work."

def fermatcheck():
    print "Input a,b,c, and n to check if they satisfy fermats last equation!"
    ainp = int(raw_input("Please input a\n"))
    binp = int(raw_input("Please input b\n"))
    cinp = int(raw_input("Please input c\n"))
    ninp = int(raw_input("Please input an n greater than 2\n"))
    fermat(ainp,binp,cinp,ninp)
fermatcheck()
    