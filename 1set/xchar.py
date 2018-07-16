#!/usr/bin/env python3

import sys
import score as sc


def _main():
    if len(sys.argv) < 2:
        sys.stderr.out('first arg must be the xor key, or -c to crack and return key, or -C to crack and print plaintext\n')
        exit(1)

    if '-c' in sys.argv or '-C' in sys.argv:
        plain = sys.stdin.buffer.read()
        key = crack(plain)
        if '-C' in sys.argv:
            sys.stdout.buffer.write(do_xor(plain, key))
        else:
            sys.stdout.write(chr(key))
    else:
        key = ord(sys.argv[1][0])
        result = do_xor(sys.stdin.buffer.read(), key)
        sys.stdout.buffer.write(result)


def do_xor(txt, key):
    if len(txt) == 0:
        return ''

    result = bytearray()
    for c in txt:
        result.append(c ^ key)

    return result


def crack(cipher):
    best_score = None
    best_key = 'a'
    for c in range(256):
        plain = do_xor(cipher, c)
        score = sc.score_english(plain)
        if best_score == None or score >= best_score:
            best_score = score
            best_key = c

    return best_key


if __name__ == '__main__':
    _main()

