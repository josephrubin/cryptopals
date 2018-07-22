#!/usr/bin/env python3
import sys
import random
import subprocess
import rbytes
import aes
import pad


def _main():
    txt = sys.stdin.buffer.read()
    sys.stdout.buffer.write(produce(txt))


def produce(txt):
    # Random 16 bytes.
    key = rbytes.count(16)

    # Append and prepend some random bytes to the input txt.
    before_count = random.randrange(5, 11)
    after_count  = random.randrange(5, 11)
    before = rbytes.count(before_count)
    after = rbytes.count(after_count)
    plain = before + txt + after

    # Pad the plaintext to a blocksize of 16.
    plain = pad.pkcs7(plain, 16)

    # Choose a mode to use.
    mode = 'ecb' if random.randrange(0, 2) == 0 else 'cbc'

    # Now do the encryption.
    if mode == 'ecb':
        cipher = aes.encrypt_ecb(plain, key)
    elif mode == 'cbc':
        random_iv = rbytes.count(16)
        cipher = aes.encrypt_cbc(plain, key, iv=random_iv)

    return cipher


if __name__ == '__main__':
    _main()

