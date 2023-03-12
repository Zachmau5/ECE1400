#!/usr/bin/python3
def getComponent(c):
    c=c.lower()
    if c=="r":
        return "Resistor"
    elif c=="c":
        return "Capacitor"
    elif c=="l":
        return "Inductor"
    elif c=="d":
        return "Diode"
    elif c=="v":
        return "Voltage Source"
    elif c=="i":
        return "Current Source"
    else:
        raise ValueError("Component {:s} is invalid".format(c))

def main():
    comp = "CViLxDRrdc"
    for c in comp:
        try:
           s=getComponent(c)
           print("{:s}\t{:s}".format(c,s))
        except ValueError as e:
           print(e)

if __name__ == "__main__":
    main()
