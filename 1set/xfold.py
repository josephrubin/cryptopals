#!/usr/bin/env python3
import sys


def _main():
    """The main function treats stdin as two strings cut in the middle.
    
    Obviously the input must be even for this to work.
    """
    inp = sys.stdin.buffer.read()

    if len(inp) % 2 != 0:
        print('must be even len string', file=sys.stderr)
        exit(1)

    half_one = inp[:int(len(inp) / 2)]
    half_two = inp[int(len(inp) / 2):]

    sys.stdout.buffer.write(xor_bytes(half_one, half_two))


def xor_bytes(a, b):
    return bytes([_a ^ _b for _a, _b in zip(a, b)])


if __name__ == '__main__':
    _main()

