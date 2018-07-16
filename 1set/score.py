#!/usr/bin/env python3

import sys
import string

# Letter: Relative Frequency (precent).
FREQ = {'a':8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.702,
        'f':2.228, 'g':2.015, 'h':6.094, 'i':6.966, 'j':0.153,
        'k':0.772, 'l':4.025, 'm':2.406, 'n':6.749, 'o':7.507,
        'p':1.929, 'q':0.095, 'r':5.987, 's':6.327, 't':9.056,
        'u':2.758, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.975,
        'z':0.074, ' ':15}
DIG_PUNC_PTS = 11 / (len(string.punctuation) + len(string.digits))
NON_PRINT_PTS = -7


def _main():
    txt = sys.stdin.buffer.read()
    score = score_english(txt)
    print(score, end='')


def score_english(txt):
    txt_len = len(txt)
    txt_hist = dict()

    # Populate a histogram of alphabet chars from the txt.
    for c in txt:
        c = chr(c)
        if c in string.ascii_letters:
            c = c.lower()
            txt_hist[c] = txt_hist.get(c, 0) + 1

    # Turn the histogram into frequencies.
    for key in txt_hist:
        val = txt_hist[key]
        txt_hist[key] = val / txt_len

    # Now calculate the score by comparing the histogram
    # to the 'ideal' frequency histogram.
    # There are many different ways to do this, look for
    # Minkowski distance, intersection kernel, chi-square,
    # Earth Mover's Distance, jenson-shannon, etc.
    score = _euclidean(txt_hist, FREQ)

    return score


def _euclidean(subject, ideal):
    total_dst = 0
    for key in ideal:
        if key in subject:
            subject_val = subject[key]
        else:
            subject_val = 0
        ideal_val = ideal[key]
        dst = (subject_val - ideal_val) ** 2
        total_dst += dst
    return -pow(total_dst, 0.5)


def _kernel(subject, ideal):
    total_dst = 0
    for key in ideal:
        if key in subject:
            subject_val = subject[key]
        else:
            subject_val = 0
        ideal_val = ideal[key]
        dst = min(subject_val, ideal_val)
        total_dst += dst
    return total_dst


if __name__ == '__main__':
    _main()

