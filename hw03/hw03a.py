#!/usr/bin/python3
import numpy as np
import math
import cmath
def quadratic(a,b,c):
#THIS SHOULD WORK
    d =(b**2-4*a*c)

    if d < 0:
        x = (-b + cmath.sqrt(d))/(2*a)
        y = (-b - cmath.sqrt(d))/(2*a)
        
    elif d == 0:
        print("you dont suck")
    else:
        x = (-b+math.sqrt(d))/(2*a)
        y = (-b-math.sqrt(d))/(2*a)
    ans = [x,y]
    return ans

def main():
    x,y = quadratic(1.7, 5,2)
    print("x={:.3f} or {:.3f}".format(x,y))
    x,y = quadratic(1,1,1)
    print("x={:.3f} or {:.3f}".format(x,y)) 
if __name__ == "__main__":
    main()
