#!/usr/bin/python3
if __name__ == "__main__":
    import sys
a = len(sys.argv)
_sum = 0
if a == 1:
    print(_sum)
else:
    for i in range(1, a):
        _sum += int(sys.argv[i])
    print(_sum)
