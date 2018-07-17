#!/usr/bin/env python3
import distance
import xchar
import sys


def _main():
    if len(sys.argv) < 2:
        print("arg one must be key, or -c to crack and print key, or -C to crack and print plaintext")
        exit(1)
    if '-c' in sys.argv:
        key = crack(sys.stdin.buffer.read())
        sys.stdout.buffer.write(key)
    elif '-C' in sys.argv:
        pass
    else:
        result = do_xor(sys.stdin.buffer.read(), sys.argv[1].encode('ascii'))
        sys.stdout.buffer.write(result)


def do_xor(txt, key):
    if len(txt) == 0 or len(key) == 0:
        return txt
    result = bytearray()
    for i, byte in enumerate(txt):
        result.append(byte ^ key[i % len(key)])
    return result


def crack(inp):
    # Find the keysize.
    distances = []
    for key_size in range(2, min(40, len(inp) // 4) + 1):
        a = inp[:key_size]
        b = inp[key_size:2*key_size]
        c = inp[2*key_size:3*key_size]
        d = inp[3*key_size:4*key_size]

        ab = distance.hamming(a, b)
        bc = distance.hamming(b, c)
        cd = distance.hamming(c, d)

        distances.append((key_size, (ab + bc + cd) / (3 * key_size)))
    distances.sort(key=lambda t: t[1])

    sizes = [k[0] for k in distances]

    choice_count = min(7, len(sizes))
    keys = []

    # Our list is sorted in order of likely keysizes.
    for i in range(choice_count):
        size = sizes[i]

        blocks = [ [ inp[k + (i * size)] for i in range(len(inp) // size) ] for k in range(size) ]
        key = bytearray()

        for block in blocks:
            key.append(xchar.crack(block))
 
        print("[" + str(size) + "]\t- ", key.decode('ascii'), file=sys.stderr)
        keys.append(key)

    return key


if __name__ == '__main__':
    _main()

