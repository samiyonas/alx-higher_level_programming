#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
a = len(sys.argv) - 1
if a != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
else:
    if sys.argv[2] == '+':
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add(int(sys.argv[1]), int(sys.argv[3]))))
        sys.exit(0)
    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub(int(sys.argv[1]), int(sys.argv[3]))))
        sys.exit(0)
    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul(int(sys.argv[1]), int(sys.argv[3]))))
        sys.exit(0)
    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], sub(int(sys.argv[1]), int(sys.argv[3]))))
