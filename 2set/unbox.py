#!/usr/bin/env python3
import sys

import prebox


def _main():
    prebox.seed()

    # First, discover the block size.
    # We will feed in a byte at a time until the same result is given for the first block.
    block_size = 2
    last = None
    while True:
        current = prebox.produce(b'a' * block_size)[:block_size]

        if current[:-1] == last:
            block_size -= 1
            break
        
        block_size += 1
        last = current
    
    # Now, detect the cipher mode.
    payload = b'a' * (block_size * 2)
    cipher = prebox.produce(payload)
    if cipher[:block_size] == cipher[block_size:block_size * 2]:
        m = 'ecb'
    else:
        m = 'cbc'
    assert m == 'ecb'

    # Now, crack the block cipher!
    plain = bytearray()
    while True:
        # Create a payload with one new byte missing.
        payload_len = (block_size - 1) - (len(plain) % block_size)
        payload = (b'a' * payload_len)
        used_blocks = (len(plain) // block_size) + 1

        # Now another new byte will slide into the last position.
        cipher = prebox.produce(payload)
        found_byte = False
        for b in range(256):
            byte = bytes([b])
            guess = payload + plain + byte
            guess_cipher = prebox.produce(guess)
            if cipher[:used_blocks * block_size] == guess_cipher[:used_blocks * block_size]:
                plain.append(b)
                found_byte = True
                break
        if not found_byte:
            break

    sys.stdout.buffer.write(plain)


if __name__ == '__main__':
    _main()
