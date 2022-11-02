#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    #start sum at 0
    sum = 0

    #loop for summing
    for arg in sys.argv[1:]:
        # sum (0(start)+value passed), store output in sum
        #int() - to cast argument into integer format
        sum += int(arg)
    print("{:d}".format(sum))
