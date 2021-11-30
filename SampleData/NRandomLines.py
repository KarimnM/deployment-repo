import sys
import os
from random import shuffle

USAGE = "First arg = number of random lines \nSecond arg = input filename \nThird arg = output filename"
if __name__ == '__main__':
    if len(sys.argv) != 4:
        exit(USAGE)

    x = 0
    try:
        x = int(sys.argv[1])
        if x < 0:
            exit("Number of lines must be a positive number")
    except Exception:
        exit(f"'{x}' is not a valid integer.")

    if not os.path.isfile(sys.argv[2]):
        exit(f"File '{sys.argv[2]}' not found.")

    lines = []
    file = open(sys.argv[2], 'r')
    line = next(file, None)
    while line is not None:
        lines += [line]
        try:
            line = next(file, None)
        except Exception:
            continue
        
    shuffle(lines)

    with open(sys.argv[3], 'w+') as f:
        f.write("".join(lines[:x]))
        
            
