import math
import argparse
import sys

def FindT(ni, a=1, b=1000, element="Si"):
    if element == "Si":
        B = 3.6e16
        EG = 1.12
    elif element == "Ge":
        B = 1.5e19
        EG = 0.67
    elif element == "GeAs":
        B = 5.5e19
        EG = 0.82
    else:
        raise ValueError("Invalid element: " + element)
    k = 8.617333262e-5 # Boltzmann constant in eV/K
    def f(T):
        return ni**2 - B * T**3 * math.exp(-EG/(k*T))
    if f(min) * f(a) >= 0:
        raise ValueError("No solution in the given range")

# =============================================================================
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("ni", type=float)
#     parser.add_argument("min", type=float, nargs="?", default=1)
#     parser.add_argument("max", type=float, nargs="?", default=1000)
#     parser.add_argument("element", type=str, nargs="?", default="Si")
#     args = parser.parse_args()
#     try:
#         T = FindT(args.ni, args.a, args.b, args.element)
#         print("T={:.2e}".format(T))
#     except ValueError as e:
#         print("No solution:", e)
#         return -1
# 
# =============================================================================

#also try this #===========================================================================
def main(args):
    if len(args) < 2:
        print("Usage: {} ni [min] [max] [element]".format(args[0]))
        return -1

    ni = float(args[1])
    min_val = float(args[2]) if len(args) > 2 else 1
    max_val = float(args[3]) if len(args) > 3 else 1000
    element = args[4] if len(args) > 4 else "Si"
    print (args[1])
    print (args[2])
    print (args[3])
    print (args[4])
    
    try:
        T = FindT(ni, min_val, max_val, element)
        print("T={:.2e}".format(T))
    except ValueError as e:
        print("No solution ", e)



# if __name__ == "__main__":
#     sys.exit(main(sys.argv))
if __name__ == "__main__":
     main()


