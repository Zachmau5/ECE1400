#!/usr/bin/python3

import sys
import hw05_lib as h5

def main():


    fileName = sys.argv[1]
    f = open(fileName)

    fResistor = []

    for line in f:
        try:
            #print(line)
            if line.strip() !="":
                fResistor.append(h5.Resistor(line.strip()))
        except ValueError as e:
            print(e)

    #fileName.close()

    for f in fResistor:
        f.print()


if __name__=="__main__":
    main()
