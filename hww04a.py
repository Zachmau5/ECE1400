#!/usr/bin/python3

import sys
def fileIO():
    try:
        if len(sys.argv) !=2:
            inFileName = input("Insert Input File Name:")
            inFile = open(inFileName,'r')

            outFileName="out.txt"
            outFile=open(outFileName,'w')

        else:
            inFileName = sys.argv[1]
            inFile = open(inFileName,'r')

            outFileName="out.txt"
            outFile=open(outFileName,'w')

        for line in inFile:
                vals= line.split(",")
                vals[0]=float(vals[0])
                vals[1]=float(vals[1])
                Sol= vals[0]+vals[1]
                print("{:.2f}+{:.2f}={:.2f}".format(vals[0],vals[1],Sol, file=outFile,end=""))
        return
        inFile.close()
        outFile.close()
    except FileNotFoundError:
        print("File Name Not Found, Try Again")


def main():
    fileIO()

if __name__=="__main__":
    main()
~              
