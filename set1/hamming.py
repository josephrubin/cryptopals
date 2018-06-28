#!/usr/bin/env python3


import sys


def compute(a, b):
    if len(a) < len(b):
        a += ('\0' * (len(b) - len(a)))
    elif len(b) < len(a):
        b += ('\0' * (len(a) - len(b)))

    dist = 0
    for c_a, c_b in zip(iter(a), iter(b)):
        s_a = bin(ord(c_a))[2:].zfill(8)
        s_b = bin(ord(c_b))[2:].zfill(8)
        for bit_a, bit_b in zip(iter(s_a), iter(s_b)):
            if bit_a != bit_b:
                dist += 1

    return dist


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("first two args msut be strings to hamming dist\n")
        exit(1)
    print(compute(sys.argv[1], sys.argv[2]))
