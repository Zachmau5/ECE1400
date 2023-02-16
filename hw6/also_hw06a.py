# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:52:35 2023

@author: halle
"""

import math
import scipy
import sys

def FindT(ni, min=1, max=1000, element="Si"):
    if element == "Si":
        B, EG = 6.83e15, 1.12
    elif element == "Ge":
        B, EG = 1.5e19, 0.67
    elif element == "GeAs":
        B, EG = 1.6e19, 0.785
    else:
        raise ValueError("Invalid element value")

    def f(T):
        return ni - B * math.pow(T, 1.5) * math.exp(-EG / (2.0 * T))

    T = None
    try:
        T = scipy.optimize.brentq(f, min, max)
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

    try:
        T = FindT(ni, min_val, max_val, element)
        print("T={:.2e}".format(T))
    except ValueError as e:
        print(str(e))
        return -1

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
