#!/usr/bin/python3

def isEven(x):
    if (x%2)==0:
        return True
    else:
        return False

def isPrime(x):
    for n in  range(2,x):
        if (x%n)==0:
            return False
    return True



def main():
    for i in range(1,21):
        if isEven(i):
            e="even"
        else:
            e="odd"
        if isPrime(i):
            p="prime"
        else:
            p="composite"
        print("{:d}\t{:s}\t{:s}".format(i,e,p))

if __name__ == "__main__":
    main()
