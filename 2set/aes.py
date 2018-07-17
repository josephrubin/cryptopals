#!/usr/bin/env python3
# This version in set2 will support CBC mode.
from Crypto.Cipher import AES
import sys
from xfold import xor_bytes as xor


def _main():
    if '-ecb' in sys.argv:
        mode = 'ecb'
        sys.argv.remove('-ecb')
    elif '-cbc' in sys.argv:
        mode = 'cbc'
        sys.argv.remove('-cbc')
    else:
        sys.stderr.write('please choose either -ecb or -cbc mode\n')
        exit(1)
      
    if '-d' in sys.argv:
        task = 'decrypt'
        sys.argv.remove('-d')
    else:
        task = 'encrypt'

    if len(sys.argv) < 2:
        sys.stderr.write('first arg must be the key')
    key = sys.argv[1]
    iv = b'\x00' *16
    txt = sys.stdin.buffer.read()

    if mode == 'ecb':
        if task == 'encrypt':
            sys.stdout.buffer.write(encrypt_ecb(txt, key))
        elif task == 'decrypt':
            sys.stdout.buffer.write(decrypt_ecb(txt, key))
    elif mode == 'cbc':
        if task == 'encrypt':
            sys.stdout.buffer.write(encrypt_cbc(txt, key))
        elif task == 'decrypt':
            sys.stdout.buffer.write(decrypt_cbc(txt, key))


def encrypt_ecb(txt, key):
    enc = AES.new(key, AES.MODE_ECB)
    return enc.encrypt(txt)


def decrypt_ecb(txt, key):
    enc = AES.new(key, AES.MODE_ECB)
    return enc.decrypt(txt)


def encrypt_cbc(txt, key, iv=(b'\x00'*16)):
    cipher = bytearray()
    for i in range(0, len(txt), 16):
        block = txt[i:i+16]
        iv = do_ecb(True, xor(iv, block), key)
        cipher.extend(iv)


def decrypt_cbc(txt, key, iv=(b'\x00*16')):
    plain = bytearray()
    for i in range(0, len(txt), 16):
        block = txt[i:i+16]
        plain.extend(xor(do_ecb(False, block, key), iv))
        iv = block


if __name__ == '__main__':
    _main()

