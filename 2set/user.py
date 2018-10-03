#!/usr/bin/env python3
import sys
import random

import rbytes
import aes
import pad


def parse(s):
    pairs = s.split('&')
    entries = dict()
    for pair in pairs:
        if '=' in pair:
            error = False
            try:
                key, val = pair.split('=')
            except ValueError:
                error = True
            if error or '=' in key or '=' in val:
                raise ValueError('malformed input: found \'=\' in the wrong place')
            if len(key) == 0:
                raise ValueError('malformed input: misplaced \'&\' or empty key')
            else:
                entries[key] = val
        elif pair == '':
            raise ValueError('malformed input: misplaced \'&.\'')
        else:
            entries[pair] = ''
    return entries


def profile_for(email):
    if '=' in email or '&' in email:
        raise ValueError('no \'=\' or \'&\' allowed in the email')
    return 'email={}&uid={}&role=user'.format(email, 10)


def oracle(email):
    # Use a consistent key.
    key = open('chal_13_key', 'rb').read()
    cipher = aes.encrypt_ecb(pad.pkcs7(profile_for(email).encode('ascii'), 16), key)
    return cipher


def unoracle(cipher):
    key = open('chal_13_key', 'rb').read()
    plain = aes.decrypt_ecb(cipher, key).decode('ascii')
    return parse(plain)


if __name__ == '__main__':
    sys.stdout.buffer.write(oracle(sys.stdin.read()))
