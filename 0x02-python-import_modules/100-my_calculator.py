#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    narg = len(sys.argv) - 1
    if narg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        #casting a & b into integers using int()
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    #calculations
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    #neither of the operators is picked
    else:
        print("Unknown operator. Available operators: +, -, * and / f")
        sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))

