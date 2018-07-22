#!/usr/bin/env python3
import sys
import random
import subprocess
import rbytes
import aes
import pad
import base64


key = None
unknown = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')


def _main():
    txt = sys.stdin.buffer.read()
    sys.stdout.buffer.write(produce(txt))


def seed():
    global key
    # Random 16 bytes.
    key = rbytes.count(16)


def produce(txt):
    assert key is not None

    # Append the unknown text.
    plain = txt + unknown

    # Pad the plaintext to a blocksize of 16.
    plain = pad.pkcs7(plain, 16)

    # Now do the encryption.
    cipher = aes.encrypt_ecb(plain, key)

    return cipher


if __name__ == '__main__':
    _main()

