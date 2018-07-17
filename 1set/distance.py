#!/usr/bin/env python3
import sys


def _main():
    if len(sys.argv) < 3:
        sys.stderr.write("first two args must be strings to hamming dist\n")
        exit(1)
    sys.stdout.write(str(hamming(sys.argv[1].encode('ascii'), sys.argv[2].encode('ascii'))))


def hamming(a, b):
    # Pad the shorter one with zeros.
    if len(a) < len(b):
        a += (b'\0' * (len(b) - len(a)))
    elif len(b) < len(a):
        b += (b'\0' * (len(a) - len(b)))

    dist = 0
    for c_a, c_b in zip(iter(a), iter(b)):
        dist += _count(c_a ^ c_b)

    return dist


def _count(binary):
    s = 0
    for c in bin(binary):
        if c == '1':
            s += 1
    return s


if __name__ == '__main__':
    _main()

