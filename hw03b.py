#!/usr/bin/python3


def main():
    arr = {"Larry":75, "Moe":85, "Curly":65, "Sleepy":48, "Happy":98}
    x= sorted(arr.items(), key=lambda item: item[0])
    for item in x:
        print("{}\t{}".format(item[0],item[1]))
    y= sorted(arr.items(), key=lambda item: item[1])
    for item in y:
        print("{}\t{}".format(item[0],item[1]))
if __name__ == "__main__":
    main()

