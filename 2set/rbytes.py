#!/usr/bin/env python3
import sys
import os

def _main():
    if len(sys.argv) < 2:
        sys.stderr.write('first arg must be byte count\n')
        exit(1)
    byte_count = int(sys.argv[1])
    sys.stdout.buffer.write(count(byte_count))


def count(byte_count):
    return os.urandom(byte_count)


if __name__ == '__main__':
    _main()

