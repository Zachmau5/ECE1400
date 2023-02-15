#!/usr/bin/python3

#import numpy as np
#import sympy as sy
import scanf

def calculator():
    a=input("> ")
    if a =="quit":
        quit
    else:

        a=a.replace(" ","")
        a=scanf.scanf("%f%c%f",a)
        #print(type(a))
        if a is None:
            print("Invalid input")
        elif a[1]==("+"):
            a1=float(a[0])
            a2=float(a[2])
            a3=a1+a2
            print(f"{a1:g} + {a2:g} = {a3:g}")
        elif a[1]==("-"):
            a1=float(a[0])
            a2=float(a[2])
            a3=a1-a2
            print(f"{a1:g} - {a2:g} = {a3:g}")

        elif a[1]==("/"):
            a1=float(a[0])
            a2=float(a[2])
            a3=a1/a2
            print(f"{a1:g} / {a2:g} = {a3:g}")

        elif a[1]==("*"):
            a1=float(a[0])
            a2=float(a[2])
            a3=a1*a2
            print(f"{a1:g} * {a2:g} = {a3:g}")

        elif a[1]!=("+","-","/","*"):
            print("Invalid operator")
        calculator()
def main():
    calculator()



if __name__ == "__main__":
    main()

