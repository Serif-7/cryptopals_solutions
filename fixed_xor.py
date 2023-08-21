#!/usr/bin/env python3
import sys


def fixed_xor(b1, b2):
    b1 = bytes.fromhex(b1)
    b2 = bytes.fromhex(b2)
    b = bytes([a ^ b for a, b in zip(b1, b2)])
    print(b)

if __name__ == '__main__':
    fixed_xor(sys.argv[1], sys.argv[2])
