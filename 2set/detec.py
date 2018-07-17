#!/usr/bin/env python3
import sys
import box


def _main():
    # We know it prepends 5 to 11 bytes.
    # So first we should ensure the first block of 16 is filled,
    # then we add two whole blocks, and then the last block is
    # of some unknown length, but it will be padded and we don't care about it.
    # (16 - 5) + 16*2 = 43
    payload = b'a' * 43

    # Now put our payload into the box.
    result = box.produce(payload)

    # Our goal is to detect whther ecb mode or cbc mode was used.
    # This is acutally pretty easy!
    # As we know, in ecb mode, the same blocks are encrypted
    # the same way. The first block and the last block will have
    # random bytes, but we completely control the second two blocks!
    # Since we put in the same plaintext for those blocks, we just need
    # to check if the ciphertexts for those blocks match.
    if result[16:32] == result[32:48]:
        mode = 'ecb'
    else:
        mode = 'cbc'

    sys.stdout.write(mode)



if __name__ == '__main__':
    _main()
