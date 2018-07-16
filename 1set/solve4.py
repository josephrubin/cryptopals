import sys
import xchar
import frombase
import score as sc


best_score = None
best_key = None
best_cipher = None
detected = None

for line in sys.stdin:
    line = frombase.from_hex(line)
    key = xchar.crack(line)
    plain = xchar.do_xor(line, key)
    score = sc.score_english(plain)
    plain = plain.decode('ascii', errors='replace')
    if best_score is None or score > best_score:
        best_cipher = line
        best_key = key
        best_score = score
        detected = plain

print(best_key, best_cipher)
print(detected)

