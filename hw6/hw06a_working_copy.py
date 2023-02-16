#!/usr/bin/python3
import scipy
import numpy as np
from scipy import optimize
import sys


#def f(x,y):
#    return np.sin(x)*x-c-y
#def solvefory(y)
#    return scipy.optimize.brentq(f, 6, 8, args=(y,1)
#def main():
#    y=-2
#    print(solvefory(-2))
#if __name__=='__main__':
#    main()
def FindT(ni, min_val, max_val, element):
    if element == "Si":
        B, EG = 6.83e15, 1.12
    elif element == "Ge":
        B, EG = 1.5e19, 0.67
    elif element == "GeAs":
        B, EG = 1.6e19, 0.785
    else:
        raise ValueError("Invalid element value")

    def f(T):
        k=8.62e-5
        return ni**2-(B*(T**3)*np.exp(-EG/(k*T)))

    try:
        T = scipy.optimize.brentq(f,min_val, max_val,)
    except ValueError:
        raise ValueError("No solution")

    return T

def main(args):
    if len(args) < 2:
        print("Usage: {} ni [min] [max] [element]".format(args[0]))
        return -1

    ni = float(args[1])
    min_val = float(args[2]) if len(args) > 2 else 1
    max_val = float(args[3]) if len(args) > 3 else 1000
    element = args[4] if len(args) > 4 else "Si"
    print (ni,min_val,max_val,element)
    try:
        T = FindT(ni, min_val, max_val, element)
        print("T={:.2e}".format(T))
    except ValueError as e:
        print(str(e))
        return -1

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
