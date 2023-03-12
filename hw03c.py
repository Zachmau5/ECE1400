#!/usr/bin/python3
import numpy as np
import math
import cmath

def diodeCurrent(Vd, Is, T, n):
    k=(1.381e-23)
    q=(1.602e-19)
    Id = (Is*((np.exp((q*Vd)/(n*k*T))-1)))
    return Id
def main():
    Vd = [0, 0.7, 1]
    for v in Vd:
       # print("Id=",diodeCurrent(v,1e-10,300,1))      
        print("Id = {:.3e} for vd = {:.3e}".format(diodeCurrent(v,1e-10,300,1),(v))) 


if __name__ == "__main__":
    main()

