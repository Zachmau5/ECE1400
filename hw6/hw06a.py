# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 08:25:17 2023

@author: halle
"""
from numpy import np
from scipy.optimize import brentq

# Constants for Si
B = 1.08e-16 # cm^3/K^3/2
Eg = 1.12 # eV
k = 8.617e-5 # eV/K

# Constants for Ge
B_Ge = 7.6e18 # cm^-3 K^-3/2
Eg_Ge = 0.66 # eV
k_Ge = 8.617e-5 # eV/K

# Constants for GeAs
B_GeAs = 8.4e18 # cm^-3 K^-3/2
Eg_GeAs = 1.52 # eV
k_GeAs = 8.617e-5 # eV/K

def FindT(ni, a, b, element):
    if element == "Si":
        B_ = B
        Eg_ = Eg
        k_ = k
    elif element == "Ge":
        B_ = B_Ge
        Eg_ = Eg_Ge
        k_ = k_Ge
    elif element == "GeAs":
        B_ = B_GeAs
        Eg_ = Eg_GeAs
        k_ = k_GeAs
    else:
        raise ValueError("Invalid element")

    def f(T):
        return ni**2-B_*(T**3)* np.exp(-Eg_ / (2 * k_ * T))

    try:
        T = brentq(f, a, b)
    except ValueError:
        raise ValueError("No solution found")

    return T
    
def main():
    #put input from sys argv locations 0,1,2 into function of 
    
    
if __name__ =="__main__":
    main()

