#!/usr/bin/env python3
import math
import sys


def _main():
    if '-x' in sys.argv:
        base = 'hex'
    elif '-b' in sys.argv:
        base = 'bin'
    else:
        print('{}: requires -x for hexidecimal or -b for binary'.format(sys.argv[0]), file=sys.stderr)
        exit(1)

    inp = sys.stdin.read()
    res = from_hex(inp) if base == 'hex' else from_bin(inp)
    sys.stdout.buffer.write(res)


def from_hex(inp): 
    return _from_base(inp, 16)


def from_bin(inp):
    return _from_base(inp, 2)


def _from_base(inp, base):
    byte_vals = bytearray()
    digits_per_byte = int(math.log(256, base))
    for i in range(0, len(inp), digits_per_byte):
        part = inp[i : i+digits_per_byte]
        if not part:
            break
        if '\n' in part:
            break
        try:
            byte_vals.append(int(part, base))
        except ValueError:
            print('invalid:', part, file=sys.stderr)
            exit(0)
    return byte_vals

if __name__ == '__main__':
    _main()

