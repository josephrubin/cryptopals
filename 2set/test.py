import sys
import aes
import pad

key = open('chal_13_key', 'rb').read()

c = aes.encrypt_ecb(pad.pkcs7(b'hello', 16), key)
c = bytearray(c)
#c[0] = 4
c = bytes(c)
print(c)

p = aes.decrypt_ecb(c, key)

print(p)
