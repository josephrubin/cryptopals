from Crypto.Cipher import AES
import sys


enc = AES.new(sys.argv[1], AES.MODE_ECB)
sys.stdout.buffer.write(enc.decrypt(sys.stdin.buffer.read()))
