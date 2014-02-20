# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math

def build_random_function(min_depth, max_depth):
    """ Creates and returns a random function, with a recursive depth betwene min_depth 
        and max_depth. It returns a nested list filled with strings representing the
        desired functions.
    """
    num = randint(1,5)
    if min_depth<=0 and max_depth>0:
        if randint(0,10)>5:
            max_depth=0
    if max_depth==0:
        num = randint(6,7) 
    if num==1:
        return ["prod",build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    if num==2:
        return ["cos_pi",build_random_function(min_depth-1,max_depth-1)]
    if num==3:
        return ["sin_pi",build_random_function(min_depth-1,max_depth-1)]
    if num==4:
        return ["ave",build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    if num==5:
        return ["sin_xy",build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    if num==6:
        return ["x"]
    if num==7:
        return ["y"]
    
def prod(a,b):
    return a*b

def cos_pi(a):
    return math.cos(math.pi*a)
    
def sin_pi(a):
    return math.sin(math.pi*a)
    
def sin_xy(a,b):
    return math.sin(math.pi*a*b*randint(1,10))

def x(a,b):
    return a

def y(a,b):
    return b
    
def ave(a,b):
    return (a+b)/2.0

def evaluate_random_function(f, x, y):
    """ Takes a function f and translates it into a series of recursive method calls
        which are then evaluated with the given x and y values.
    """
    str = f[0]
    if str=='ave':
        return ave(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    if str=='prod':
        return prod(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    if str=='sin_xy':
        return sin_xy(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    if str=='cos_pi':
        return cos_pi(evaluate_random_function(f[1],x,y))
    if str=='sin_pi':
        return sin_pi(evaluate_random_function(f[1],x,y))
    if str=='x':
        return x
    if str=='y':
        return y

            
            
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    return(output_interval_end-output_interval_start)*float((val-input_interval_start))/float((input_interval_end-input_interval_start))+output_interval_start

def main():
    red = build_random_function(4,17)
    green = build_random_function(3,18)
    blue = build_random_function(2,20)
    im = Image.new("RGB",(350,350))
    horz,vert = im.size
    pixels = im.load()
    for i in xrange(horz):
        x = remap_interval(i,0,horz,-1,1)
        for j in xrange(vert):
              y = remap_interval(j,0,horz,-1,1)
              r = evaluate_random_function(red,x,y)
              g = evaluate_random_function(green,x,y)
              b = evaluate_random_function(blue,x,y)
              r = int(remap_interval(r,-1,1,0,255))
              g = int(remap_interval(g,-1,1,0,255))
              b = int(remap_interval(b,-1,1,0,255))
              pixels[i,j] = (r,g,b)
              
    im.save("Deniz9","png")
              
if __name__=="__main__":
    main()      