#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    total = 0
    num = len(sys.argv) - 1
    if num == 0:
        print("{}".format(num))
    else:
        for i in range(num):
            total += sys.argv[i + 1]
        print("{}".format(total))
