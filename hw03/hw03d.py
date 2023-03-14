#!/usr/bin/python3
import numpy as np
import sympy as sym

def solve(A,B,C,D,E,F):
    x,y=sym.symbols('x,y')
    eq1 = sym.Eq(A*x+B*y,C)
    eq2 = sym.Eq(D*x+E*y,F)
    result = sym.solve([eq1,eq2],(x,y))
    return float(result[x]), float(result[y])
def main():
    x,y =solve(2,5,7,4,-6,12)
    print("x = {:.2f}\ty = {:.2f}\n".format(x,y))    
if __name__ == "__main__":
    main()


