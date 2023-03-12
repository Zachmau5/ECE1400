#!/usr/bin/python3
import scipy
import numpy as np
from scipy import optimize
import sys


def FindT(ni, min_val, max_val, element):
    if element == "Si":
        B, EG =1.08e31 , 1.12
    elif element == "Ge":
        B, EG = 2.31e30, 0.66
    elif element == "GeAs":
        B, EG = 1.27e29, 1.42
    else:
        print("No Solution")
        sys.exit(-1)
    T = optimize.brentq(f,min_val, max_val,args=(ni,B, EG))
    return T

def f(T, ni, B, EG):
    k=8.62e-5
    return B*T**3*np.exp(-(EG/(k*T)))-ni**2

def main():
    min_val=1
    max_val=1e3
    element=1.12
    vals=sys.argv
    l = len(sys.argv)

    if l ==1:
        print("No solution")
        sys.exit(-1)

    if l==2:
        ni=float(vals[1])
        element="Si"

    elif l ==5:
        ni=float(vals[1])
        min_val=float(vals[2])
        max_val=float(vals[3])
        element=vals[4]
    T = FindT(ni, min_val, max_val, element)
    print("T={:.2e}".format(T))

if __name__ == "__main__":
    main()
