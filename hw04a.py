!/usr/bin/python3

import sys
def fileIO():
    try:
        if len(sys.argv) ==1:
            inFileName = input("Please enter an input filename: ")

            outFileName="out.txt"
        elif len(sys.argv) ==2:
            inFileName = sys.argv[1]

            outFileName="out.txt"
        else:
            inFileName = sys.argv[1]

            outFileName= sys.argv[2]
        inFile = open(inFileName,'r')
        outFile = open(outFileName,'w')
        for line in inFile:
                vals= line.strip().split(",")
                vals[0]=float(vals[0])
                vals[1]=float(vals[1])
                Sol= vals[0]+vals[1]
                out= "{:.2f} + {:.2f} = {:.2f}".format(vals[0],vals[1],Sol)
                print(out)
                print(out,file=outFile)
        inFile.close()
        outFile.close()
    except FileNotFoundError:
        print("File Name Not Found, Try Again")


def main():
    fileIO()

if __name__=="__main__":
    main()
