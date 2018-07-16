import sys
import string

def main():
    sys.stdout.write(str(calculate_score(sys.stdin.buffer.read())))


DIST = {'a':8,
        'b':1,
        'c':3,
        'd':4,
        'e':13,
        'f':2,
        'g':2,
        'h':6,
        'i':7,
        'j':0,
        'k':1,
        'l':4,
        'm':2,
        'n':7,
        'o':8,
        'p':2,
        'q':0,
        'r':6,
        's':6,
        't':9,
        'u':3,
        'v':1,
        'w':2,
        'x':0,
        'y':2,
        'z':0,
        ' ':20}
def calculate_score(inp):
    dist = {}
    score = 0
    alph = (string.ascii_letters + ' ').encode('ascii')
    for c in inp:
        if c in alph:
            c = chr(c).lower()
            if c in dist:
                dist[c] += 1
            else:
                dist[c] = 1
        else:
            score -= 12
    for key in dist:
        score += dist[key] * DIST[key]
    return score


main()
