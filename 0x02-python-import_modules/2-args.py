#!/usr/bin/python3
if __name__ == "__main__":
    import sys
a = len(sys.argv) - 1
if a == 0:
    print("{} arguments.".format(a))
elif a == 1:
    print("{} argument:".format(a))
    print("{}: {}".format(a, sys.argv[a]))
else:
    print("{} arguments:".format(a))
    for i in range(1, a + 1):
        print("{}: {}".format(i, sys.argv[i]))
