#!/usr/bin/env python3


import sys


def compute(a, b):
    if len(a) < len(b):
        a += (b'\0' * (len(b) - len(a)))
        print("Fill first string with 0s")
    elif len(b) < len(a):
        b += (b'\0' * (len(a) - len(b)))
        print("Fill second string with 0s")

    dist = 0
    for c_a, c_b in zip(iter(a), iter(b)):
        dist += count(c_a ^ c_b)

    return dist


def count(binary):
    s = 0
    for c in bin(binary):
        if c == '1':
            s += 1
    return s


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("first two args must be strings to hamming dist\n")
        exit(1)
    print(compute(sys.argv[1].encode('ascii'), sys.argv[2].encode('ascii')))
