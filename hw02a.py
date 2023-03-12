#!/usr/bin/python3

def forLoop():
    for x in range(1,6):
   	 print(x)

def whileLoop():
    x=0
    while x<6:
        x = x+1
        if x==6:
            break
        print(x) 

def main():
    forLoop()
    whileLoop()


if __name__ == "__main__":
    main()
