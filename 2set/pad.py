#!/usr/bin/env python3
import sys


def _main():
    if len(sys.argv) < 2:
        sys.stderr.write("first arg must be block size\n")
        exit(1)

    txt = sys.stdin.buffer.read()
    block_size = int(sys.argv[1])
    sys.stdout.buffer.write(pkcs7(txt, block_size))


def pkcs7(txt, block_size):
    missing_byte_count = block_size - len(txt) % block_size

    if missing_byte_count > 255:
        sys.stderr.write('pkcs7 padding is not well defined for a block_size above 255,\
                          because that is the highest value of a single byte!')
        exit(1)

    return txt + bytes([missing_byte_count]) * missing_byte_count


if __name__ == '__main__':
    _main()

